# Copyright 2020 Cognicept Systems
# Author: Jakub Tomasek (jakub@cognicept.systems)
# --> AgentLifeCycle handles life cycle of Cognicept Agents

import docker
import boto3
import base64
import json
import os
import dateutil
from datetime import datetime
import re
import glob

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class AgentLifeCycle:
    _docker_container_names = ["cgs_agent","cgs_diagnostics_agent","remote_intervention_agent","ecs_server","cgs_diagnostics_ecs_api","cgs_diagnostics_streamer_api","rosbridge"]
    _docker_images = {}
    _docker_images["remote_intervention_agent"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/remote_intervention_agent"
    _docker_images["cgs_agent"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/cognicept_rosbridge_listener_agent"
    _docker_images["cgs_diagnostics_agent"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/cognicept_diagnostics_agent"
    _docker_images["ecs_server"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/cognicept_rosbridge_listener_agent"
    _docker_images["cgs_diagnostics_ecs_api"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/cognicept_diagnostics_api"
    _docker_images["cgs_diagnostics_streamer_api"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/cognicept_diagnostics_api"
    _docker_images["rosbridge"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/orbitty"
    _docker_images["orbitty"] = "412284733352.dkr.ecr.ap-southeast-1.amazonaws.com/orbitty"
    def get_latest_log_loc(object, args):
        # get latest log location
        latest_log_loc_file_path = os.path.expanduser(args.path+"agent/logs/latest_log_loc.txt")
        latest_log_loc = ""
        try:            
            with open(latest_log_loc_file_path) as txt_file:                
                latest_log_loc_temp = txt_file.readline()
                latest_log_loc_temp = latest_log_loc_temp[:-1]
                latest_log_loc = latest_log_loc_temp.replace("/$HOME/.cognicept/","")
        except:
            cgs_agent_status = f"{bcolors.FAIL}UNKNOWN{bcolors.ENDC}"
        
        return latest_log_loc

    def get_status(object, args):
        client = docker.from_env()

        # check status of cgs_agent
        # get latest log location
        latest_log_loc = object.get_latest_log_loc(args)
        
        # read latest status and set for display
        file_path = os.path.expanduser(args.path+latest_log_loc+"/logDataStatus.json")        
        try:            
            with open(file_path) as json_file:                
                data = json.load(json_file)
                period_since_update = datetime.utcnow() - dateutil.parser.parse(data["timestamp"])
                if(period_since_update.seconds < 30 and period_since_update.seconds >= 0):
                    cgs_agent_status = bcolors.OKBLUE + data["message"].upper() + bcolors.ENDC
                else:
                    cgs_agent_status = f"{bcolors.WARNING}STALE{bcolors.ENDC}"

        except:
            cgs_agent_status = f"{bcolors.FAIL}ERROR{bcolors.ENDC}"


        for container_name in object._docker_container_names:
            print(container_name, end = ': ', flush=True)
            try:
                container = client.containers.get(container_name)
                if container.status != "running":
                    print(f"{bcolors.WARNING}OFFLINE{bcolors.ENDC}")
                else:
                    if(container_name == "cgs_agent"):
                        print(cgs_agent_status)
                    elif(container_name == "remote_intervention_agent"):
                        object.parseRemoteInterventionAgentLogs(container.logs(tail=50))
                    elif(container_name == "cgs_diagnostics_agent"):
                        print(cgs_agent_status)                        
                    else:
                        print(f"{bcolors.OKBLUE}ONLINE{bcolors.ENDC}")
            except docker.errors.NotFound:
                print(f"{bcolors.FAIL}CONTAINER NOT FOUND{bcolors.ENDC}")
    
    def get_last_event(object, args):
        
        # get latest log location
        latest_log_loc = object.get_latest_log_loc(args)
        
        # read and display latest log if any
        file_path = os.path.expanduser(args.path+latest_log_loc)        
        try:
            print(f"{bcolors.OKBLUE}Looking for the latest event log...{bcolors.ENDC}")
            # should read only latest logData#.json file and not logDataStatus.json
            list_of_log_files = [fn for fn in glob.glob(file_path + "/*.json") \
                                    if not os.path.basename(fn).endswith("logDataStatus.json")]
            latest_log_file = max(list_of_log_files, key=os.path.getctime)            
            
            with open(latest_log_file) as json_file:                
                data = json.load(json_file)
                print(f"{bcolors.OKGREEN}Latest Event Log:{bcolors.ENDC}")
                print(json.dumps(data, indent=4, sort_keys=True))                
        except:
            print(f"{bcolors.WARNING}No event logs present.{bcolors.ENDC}")

    def parseRemoteInterventionAgentLogs(object, logs):
        ## Parses logs to find status of remote intervention agent
        logs_lines = logs.splitlines()
        # parse logs to get current status
        ri_agent_status = {}
        ri_agent_status["AGENT"] = ""
        ri_agent_status["WEBRTC"] = ""
        ri_agent_status["WEBSOCKET"] = ""

        # find latest status of the each module (agent, webrtc, websocket)
        for line in reversed(logs_lines):
            for key,value in ri_agent_status.items():
                if(value != ""):
                    continue
                matches = re.search(rf'^.*{key}:: STATUS:: (?P<status>.*)\\.*$', str(line))
                if(matches is not None):
                    ri_agent_status[key] = matches.groups(0)[0]
            if(ri_agent_status["AGENT"] != "" and ri_agent_status["WEBRTC"] != "" and ri_agent_status["WEBSOCKET"] != ""):
                continue
        
        output_text = f"{bcolors.OKBLUE}ONLINE{bcolors.ENDC}"
        for key,value in ri_agent_status.items():
            if(value == ""):
                #if not found, it was not yet initialized
                output_text = f"{bcolors.WARNING} NOT INITIALIZED {bcolors.ENDC}"
                break
            if(value != "OK"):
                output_text = f"{bcolors.WARNING} {key} {value} {bcolors.ENDC}"
                break
        print(output_text)

    def restart(object, args):
        print("Restarting agents")
        object.remove_agents(args)
        object.run(args)

    def remove_agents(object, args):   
        client = docker.from_env()
        print("STOP: ")
        for container_name in object._docker_container_names:
            print("   - " + container_name, end = ': ', flush=True)
            try:
                container = client.containers.get(container_name)
                container.stop(timeout=10)
                container.remove()
                print(f"{bcolors.OKBLUE}DONE{bcolors.ENDC}")
            except docker.errors.NotFound:
                print(f"{bcolors.WARNING}NOT FOUND{bcolors.ENDC}")                	
            except docker.errors.APIError:
                print(f"{bcolors.FAIL}ERROR{bcolors.ENDC}")
    
    def run(object, args):
        args.config.load_config(args.path)
        object._agent_run_options = {}
        object._agent_run_options["cgs_agent"] = {"command": "start_cognicept_agent.py","volumes":{args.config.config_path + "agent/logs/": {"bind": "/app/logs", "mode":"rw"}},"network_mode": "host"}
        object._agent_run_options["cgs_diagnostics_agent"] = {"command": "roslaunch rosrect-listener-agent listener-agent.launch" ,"volumes":{args.config.config_path + "agent/logs/": {"bind": "/root/.cognicept/agent/logs", "mode":"rw"}} ,"network_mode": "host"}        
        object._agent_run_options["ecs_server"] = {"command": "/ecs_api_server/ecs_endpoint.py","network_mode": "host"}
        object._agent_run_options["cgs_diagnostics_ecs_api"] = {"command": "/ecs_api_server/ecs_endpoint.py" ,"network_mode": "host"}
        object._agent_run_options["cgs_diagnostics_streamer_api"] = {"command": "/data_streamer/streamer_endpoint.py" ,"network_mode": "host"}
        object._agent_run_options["remote_intervention_agent"] = {"command": "rosrun remote_intervention_agent cognicept_agent_node" ,"network_mode": "host"}        
        object._agent_run_options["rosbridge"] = {"command": "roslaunch rosbridge_server rosbridge_websocket.launch" ,"network_mode": "host"}  
        client = docker.from_env()
        print("RUN: ")
        for container_name in object._docker_container_names:
            print("   - " + container_name, end = ': ', flush=True)
            try:
                options = object._agent_run_options[container_name]
                options["name"] = container_name
                options["detach"] = True
                options["environment"] = args.config.config
                options["restart_policy"] = {"Name":"unless-stopped"}
                options["tty"] = True
                command = options.pop("command")
                container = client.containers.run(object._docker_images[container_name], command, **options)
                print(f"{bcolors.OKBLUE}DONE{bcolors.ENDC}")
            except docker.errors.ContainerError:
                print(f"{bcolors.WARNING}ALREADY EXISTS{bcolors.ENDC} (run `cognicept update`)")
            except docker.errors.ImageNotFound:
                print(f"{bcolors.WARNING}IMAGE NOT FOUND{bcolors.ENDC} (run `cognicept update`)")
            except docker.errors.APIError:
                print(f"{bcolors.FAIL}DOCKER ERROR{bcolors.ENDC}")
    
    def run_orbitty(object, args):
        args.config.load_config(args.path)
        os.system("xhost +local:root")
        client = docker.from_env()
        try:
            options = {}
            options["name"] = "orbitty"
            options["detach"] = False
            options["privileged"] = True
            options["volumes"] = {}
            options["volumes"][args.config.config_path] = {"bind": "/config", "mode":"rw"}
            options["volumes"]["/tmp/.X11-unix"] = {"bind": "/tmp/.X11-unix", "mode":"rw"}
            environment = args.config.config
            environment["QT_X11_NO_MITSHM"] = 1
            environment["DISPLAY"] = ":0"
            options["environment"] = args.config.config
            options["remove"] = True
            options["tty"] = True
            command = "roslaunch orbitty orbitty.launch"
            client.containers.run(object._docker_images["orbitty"], command, **options)
        except docker.errors.ContainerError:
            print(f"{bcolors.WARNING}ALREADY RUNNING{bcolors.ENDC}")
        except docker.errors.ImageNotFound:
            print(f"{bcolors.WARNING}IMAGE NOT FOUND{bcolors.ENDC} (run `cognicept update`)")
        except docker.errors.APIError:
            print(f"{bcolors.FAIL}DOCKER ERROR{bcolors.ENDC}")
        os.system("xhost -local:root")

    def update(object, args):
        print("Info: This may take a while depending on your connection.")
        args.config.load_config(args.path)
        ecr_client = boto3.client('ecr', region_name='ap-southeast-1', aws_access_key_id=args.config.config["AWS_ACCESS_KEY_ID"], aws_secret_access_key = args.config.config["AWS_SECRET_ACCESS_KEY"])
        
        

        token = ecr_client.get_authorization_token()
        username, password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode().split(':')
        registry = token['authorizationData'][0]['proxyEndpoint']        

        docker_client = docker.from_env()
        try:
            result = docker_client.login(username, password, registry=registry, reauth=True)
        except docker.errors.APIError:
            print("You don't have ECR repository permissions. Check you AWS credentials with Cognicept team.")

        for container_name, image_name in object._docker_images.items():
            print(image_name)
            result = docker_client.images.pull(image_name, tag="latest")

        print("Info: Run `cognicept restart` to redeploy updated agents.")
        
