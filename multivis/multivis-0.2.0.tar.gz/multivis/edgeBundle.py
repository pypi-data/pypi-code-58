import os
import sys
from string import Template
import numpy as np
import pandas as pd
#import socket
import webbrowser as wb
import matplotlib
import matplotlib.pyplot as plt
from .utils import *
import json

class edgeBundle:
    """Class for edgeBundle to produce a hierarchical edge bundle.

        Parameters
        ----------
        edges : Pandas dataframe containing edges generated from Edge.
        nodes : Pandas dataframe containing nodes generated from Edge.

        Methods
        -------
        set_params : Set parameters -
            html_file: Name to save the HTML file as (default: 'hEdgeBundle.html')
            innerRadiusOffset: Sets the inner radius based on the offset value from the canvas width/diameter (default: 120)
            blockSeparation: Value to set the distance between different segmented blocks (default: 1)
            linkFadeOpacity: The link fade opacity when hovering over/clicking nodes (default: 0.05)
            mouseOver: Setting to 'True' swaps from clicking to hovering over nodes to select them (default: True)
            fontSize: The font size in pixels set for each node (default: 10)
            backgroundColor: Set the background colour of the plot (default: 'white')
            foregroundColor: Set the foreground colour of the plot (default: 'black')
            node_data: Peak Table column names to include in the mouse over information (default: 'Name' and 'Label')
            nodeColorScale: The scale to use for colouring the nodes ("linear", "reverse_linear", "log", "reverse_log", "square", "reverse_square", "area", "reverse_area", "volume", "reverse_volume", "ordinal") (default: 'linear')
            node_color_column: The Peak Table column to use for node colours (default: None sets to black)
            node_cmap: Set the CMAP colour palette to use for colouring the nodes (default: 'brg')
            edgeColorScale: The scale to use for colouring the edges, if edge_color_value is 'pvalue' ("linear", "reverse_linear", "log", "reverse_log", "square", "reverse_square", "area", "reverse_area", "volume", "reverse_volume", "ordinal") (default: 'linear')
            edge_color_value: Set the values to colour the edges by. Either 'score or 'pvalue' (default: 'score')
            edge_cmap: Set the CMAP colour palette to use for colouring the edges (default: 'brg')

        build : Generates the JavaScript embedded HTML code and writes to a HTML file and opens it in a browser.
        buildDashboard : Generates the JavaScript embedded HTML code in a dashboard format, writes to a HTML file and opens it in a browser.
    """

    def __init__(self, nodes, edges):

        self.__nodes = self.__checkNodes(nodes);
        self.__edges = self.__checkEdges(edges);

        self.set_params()

    def set_params(self, html_file='hEdgeBundle.html', innerRadiusOffset=120, blockSeparation=1, linkFadeOpacity=0.05, mouseOver=True, fontSize=10, backgroundColor='white', foregroundColor='black', node_data=['Name', 'Label'], nodeColorScale='linear', node_color_column='none', node_cmap='brg', edgeColorScale='linear', edge_color_value='score', edge_cmap="brg"):

        html_file, innerRadiusOffset, blockSeparation, linkFadeOpacity, mouseOver, fontSize, backgroundColor, foregroundColor, node_data, nodeColorScale, node_color_column, node_cmap, edgeColorScale, edge_color_value, edge_cmap = self.__paramCheck(html_file, innerRadiusOffset, blockSeparation, linkFadeOpacity, mouseOver, fontSize, backgroundColor, foregroundColor, node_data, nodeColorScale, node_color_column, node_cmap, edgeColorScale, edge_color_value, edge_cmap)

        self.__html_file = html_file;
        self.__innerRadiusOffset = innerRadiusOffset;
        self.__blockSeparation = blockSeparation;
        self.__linkFadeOpacity = linkFadeOpacity;
        self.__mouseOver = mouseOver;
        self.__fontSize = fontSize;
        self.__backgroundColor = backgroundColor;
        self.__foregroundColor = foregroundColor;
        self.__node_data = node_data;
        self.__nodeColorScale = nodeColorScale;
        self.__node_color_column = node_color_column;
        self.__node_cmap = node_cmap;
        self.__edgeColorScale = edgeColorScale;
        self.__edge_color_value = edge_color_value;
        self.__edge_cmap = edge_cmap;

    def __process_params(self):

        nodes = self.__nodes
        edges = self.__edges
        mouseOver = self.__mouseOver

        nodes, edges = self.__node_color(nodes, edges)
        edges = self.__edge_color(edges)

        if mouseOver:
            mouse = "true";
        else:
            mouse = "false";

        bundleJson = self.__df_to_Json(nodes, edges);

        return bundleJson, mouse

    def build(self):

        backgroundColor = self.__backgroundColor
        foregroundColor = self.__foregroundColor
        innerRadiusOffset = self.__innerRadiusOffset
        blockSeparation = self.__blockSeparation
        linkFadeOpacity = self.__linkFadeOpacity
        fontSize = self.__fontSize
        html_file = self.__html_file

        bundleJson, mouse = self.__process_params()

        css_text_template_bundle = Template(self.__getCSS());
        js_text_template_bundle = Template(self.__getJS())
        html_template_bundle = Template(self.__getHTML());

        js_text = js_text_template_bundle.substitute({'flareData': bundleJson
                                                         , 'innerRadiusOffset': innerRadiusOffset
                                                         , 'blockSeparation': blockSeparation
                                                         , 'linkFadeOpacity': linkFadeOpacity
                                                         , 'fontSize': fontSize
                                                         , 'mouseOver': mouse
                                                         , 'backgroundColor': backgroundColor})

        css_text = css_text_template_bundle.substitute({'backgroundColor': backgroundColor, 'foregroundColor': foregroundColor})

        html = html_template_bundle.substitute({'css_text': css_text, 'js_text': js_text})

        with open(html_file, 'w') as f:
            f.write(html)
            f.close()

        print("HTML writen to {}".format(html_file))

        wb.open('file://' + os.path.realpath(html_file))

    def buildDashboard(self):

        backgroundColor = self.__backgroundColor
        foregroundColor = self.__foregroundColor
        innerRadiusOffset = self.__innerRadiusOffset
        blockSeparation = self.__blockSeparation
        linkFadeOpacity = self.__linkFadeOpacity
        fontSize = self.__fontSize
        html_file = self.__html_file
        node_data = self.__node_data

        bundleJson, mouse = self.__process_params()

        css_text_template_bundle = Template(self.__getCSSdashboard());
        js_text_template_bundle = Template(self.__getJSdashboard());
        html_template_bundle = Template(self.__getHTMLdashboard());

        js_text = js_text_template_bundle.substitute({'flareData': bundleJson
                                                         , 'innerRadiusOffset': innerRadiusOffset
                                                         , 'blockSeparation': blockSeparation
                                                         , 'linkFadeOpacity': linkFadeOpacity
                                                         , 'fontSize': fontSize
                                                         , 'mouseOver': mouse
                                                         , 'node_data': {'data': node_data}
                                                         , 'backgroundColor': backgroundColor})

        css_text = css_text_template_bundle.substitute({'backgroundColor': backgroundColor, 'foregroundColor': foregroundColor})

        html = html_template_bundle.substitute({'css_text': css_text, 'js_text': js_text})

        html_file = html_file.split(".")[0] + "_dashboard.html"

        with open(html_file, 'w') as f:
            f.write(html)
            f.close()

        print("HTML writen to {}".format(html_file))

        wb.open('file://' + os.path.realpath(html_file))

    def __checkNodes(self, nodes):

        if not isinstance(nodes, pd.DataFrame):
            print("Error: A dataframe was not entered. Please check your data.")
            sys.exit()

        nodes_col = ['Name', 'Label']

        for value in nodes_col:
            if value not in nodes.columns:
                print("Error: Nodes dataframe items not valid. Include the following {}.".format('and '.join(nodes_col)))
                sys.exit()

        return nodes

    def __checkEdges(self, edges):

        if not isinstance(edges, pd.DataFrame):
            print("Error: A dataframe was not entered. Please check your data.")
            sys.exit()

        edges_col = ['start_index', 'start_name', 'start_label', 'end_index', 'end_name', 'end_label', ]

        for value in edges_col:
            if value not in edges.columns:
                print("Error: Edges dataframe items not valid. Include the following {} , and either \"Pvalue\" or \"Score\" and \"sign\".".format(', '.join(edges_col)))
                sys.exit()

        if "pvalue" not in edges.columns or "score" not in edges.columns:
            print("Error: Edges dataframe does not contain either \"Pvalue\" or \"Score\".")
            sys.exit()

        return edges

    def __paramCheck(self, html_file, innerRadiusOffset, blockSeparation, linkFadeOpacity, mouseOver, fontSize, backgroundColor, foregroundColor, node_data, nodeColorScale, node_color_column, node_cmap, edgeColorScale, edge_color_value, edge_cmap):

        nodes = self.__nodes
        col_list = list(nodes.columns) + ['none']

        if not isinstance(html_file, str):
            print("Error: Html file is not valid. Choose a string value.")
            sys.exit()
        else:
            html_end = html_file.split(".")[-1]

            if html_end != "html":
                print("Error: Html file extension is not 'html'. Please use '.html' extension.")
                sys.exit()

        if not isinstance(innerRadiusOffset, float):
            if not isinstance(innerRadiusOffset, int):
                print("Error: Inner radius offset is not valid. Choose a float or integer value.")
                sys.exit()

        if not isinstance(blockSeparation, float):
            if not isinstance(blockSeparation, int):
                print("Error: Block separation is not valid. Choose a float or integer value.")
                sys.exit()

        if not isinstance(linkFadeOpacity, float):
            if not isinstance(linkFadeOpacity, int):
                print("Error: Link fade opacity is not valid. Choose a float or integer value.")
                sys.exit()

        if not type(mouseOver) == bool:
            print("Error: Mouse over is not valid. Choose either \"True\" or \"False\".")
            sys.exit()

        if not isinstance(fontSize, float):
            if not isinstance(fontSize, int):
                print("Error: Font size is not valid. Choose a float or integer value.")
                sys.exit()

        if not matplotlib.colors.is_color_like(backgroundColor):
            print("Error: Background colour is not valid. Choose a valid colour value.")
            sys.exit()

        if not matplotlib.colors.is_color_like(foregroundColor):
            print("Error: Slider text colour is not valid. Choose a valid colour value.")
            sys.exit()

        if not isinstance(node_data, list):
                print("Error: Node data is not valid. Use a list.")
                sys.exit()
        else:
            for node_item in node_data:
                if node_item not in col_list:
                    print("Error: Node data item not valid. Choose one of {}.".format(', '.join(col_list)))
                    sys.exit()

            if "Name" not in node_data:
                print("Error: Column \"Name\" should be node data. Please correct")
                sys.exit()

            if "Label" not in node_data:
                print("Error: Column \"Label\" should be node data. Please correct")
                sys.exit()

        if nodeColorScale.lower() not in ["linear", "reverse_linear", "log", "reverse_log", "square", "reverse_square", "area", "reverse_area", "volume", "reverse_volume", "ordinal"]:
            print("Error: Node color scale type not valid. Choose either \"linear\", \"reverse_linear\", \"log\", \"reverse_log\", \"square\", \"reverse_square\", \"area\", \"reverse_area\", \"volume\", \"reverse_volume\", \"ordinal\".")
            sys.exit()

        if node_color_column not in col_list:
            print("Error: Node color column not valid. Choose one of {}.".format(', '.join(col_list)))
            sys.exit()
        else:
            if node_color_column != 'none':
                node_color_values = np.array(nodes[node_color_column].values)

                if nodeColorScale != 'ordinal':
                    try:
                        float(node_color_values[0])
                    except ValueError:
                        if not matplotlib.colors.is_color_like(node_color_values[0]):
                            print("Error: Node colour column is not valid. While colorScale is not ordinal, choose a column containing colour values, floats or integer values.")
                            sys.exit()

        if not isinstance(node_cmap, str):
            print("Error: Node CMAP is not valid. Choose a string value.")
            sys.exit()
        else:
            cmap_list = matplotlib.cm.cmap_d.keys()

            if node_cmap not in cmap_list:
                print("Error: Node CMAP is not valid. Choose one of the following: {}.".format(', '.join(cmap_list)))
                sys.exit()

        if edgeColorScale.lower() not in ["linear", "reverse_linear", "log", "reverse_log", "square", "reverse_square", "area", "reverse_area", "volume", "reverse_volume", "ordinal"]:
            print("Error: Node color scale type not valid. Choose either \"linear\", \"reverse_linear\", \"log\", \"reverse_log\", \"square\", \"reverse_square\", \"area\", \"reverse_area\", \"volume\", \"reverse_volume\", \"ordinal\".")
            sys.exit()

        if edge_color_value.lower() not in ["pvalue", "score"]:
            print("Error: Colour scale type not valid. Choose either \"Pvalue\" or \"Score\".")
            sys.exit()

        if not isinstance(edge_cmap, str):
            print("Error: Edge CMAP is not valid. Choose a string value.")
            sys.exit()
        else:
            cmap_list = matplotlib.cm.cmap_d.keys()

            if edge_cmap not in cmap_list:
                print("Error: Edge CMAP is not valid. Choose one of the following: {}.".format(', '.join(cmap_list)))
                sys.exit()

        return html_file, innerRadiusOffset, blockSeparation, linkFadeOpacity, mouseOver, fontSize, backgroundColor, foregroundColor, node_data, nodeColorScale, node_color_column, node_cmap, edgeColorScale, edge_color_value, edge_cmap

    def __df_to_flareJson(self, nodes, edges):
        """Convert dataframes into nested JSON as in flare files used for D3.js"""

        nodeList = list(nodes.columns)

        if "Idx" in nodeList:
            nodeList.remove('Idx')

        if "Label" in nodeList:
            nodeList.remove('Label')

        if "color" in nodeList:
            nodeList.remove('color')

        if "block" in nodeList:
            nodeList.remove('block')

        nodeData = nodes[nodeList]
        nodeDataList = list(nodeData.drop(columns=['Name']).columns)

        flare = dict()
        d = {"Name": "flare", "children": []}

        for index, row in edges.iterrows():

            if len(row) > 12:
                parent_index = row[0]
                parent_name = row[1]
                parent_color = row[2]
                parent_label = row[3]
                parent_block = row[4]
                child_index = row[5]
                child_name = row[6]
                child_color = row[7]
                child_label = row[8]
                child_block = row[9]
                link_score = row[10]
                link_sign = row[11]
                link_pvalue = row[12]
                link_color = row[13]

                # Make a list of keys
                key_list = []
                for item in d['children']:
                    key_list.append(item['id'])

                # if parent index is NOT a key in flare.JSON, append it
                if not parent_index in key_list:

                    parent_dic = {"id": parent_index, "Name": parent_name, "Label": parent_label, "node_color": parent_color, "block": parent_block}

                    for col in nodeDataList:
                        parent_dic[col] = list(nodeData[nodeData.Name.isin([parent_name])][col])[0]

                    child_dic = {"id": child_index, "Name": child_name, "Label": child_label, "node_color": child_color, "link_score": link_score, "link_sign": link_sign, "link_pvalue": link_pvalue, "block": child_block, "link_color": link_color}

                    for col in nodeDataList:
                        child_dic[col] = list(nodeData[nodeData.Name.isin([child_name])][col])[0]

                    parent_dic["children"] = [child_dic]

                    d['children'].append(parent_dic)

                # if parent index IS a key in flare.json, add a new child to it
                else:

                    child_dic = {"id": child_index, "Name": child_name, "Label": child_label, "node_color": child_color, "link_score": link_score, "link_sign": link_sign, "link_pvalue": link_pvalue, "block": child_block, "link_color": link_color}

                    for col in nodeDataList:
                        child_dic[col] = list(nodeData[nodeData.Name.isin([child_name])][col])[0]

                    d['children'][key_list.index(parent_index)]['children'].append(child_dic)
            else:
                parent_index = row[0]
                parent_name = row[1]
                parent_color = row[2]
                parent_label = row[3]
                child_index = row[4]
                child_name = row[5]
                child_color = row[6]
                child_label = row[7]
                link_score = row[8]
                link_sign = row[9]
                link_pvalue = row[10]
                link_color = row[11]

                # Make a list of keys
                key_list = []
                for item in d['children']:
                    key_list.append(item['id'])

                # if parent index is NOT a key in flare.JSON, append it
                if not parent_index in key_list:

                    parent_dic = {"id": parent_index, "Name": parent_name, "Label": parent_label, "node_color": parent_color}

                    for col in nodeDataList:
                        parent_dic[col] = list(nodeData[nodeData.Name.isin([parent_name])][col])[0]

                    child_dic =  {"id": child_index, "Name": child_name, "Label": child_label, "node_color": child_color, "link_score": link_score, "link_sign": link_sign, "link_pvalue": link_pvalue, "link_color": link_color}

                    for col in nodeDataList:
                        child_dic[col] = list(nodeData[nodeData.Name.isin([child_name])][col])[0]

                    parent_dic["children"] = [child_dic]

                    d['children'].append(parent_dic)

                # if parent index IS a key in flare.json, add a new child to it
                else:

                    child_dic = {"id": child_index, "Name": child_name, "Label": child_label, "node_color": child_color, "link_score": link_score, "link_sign": link_sign, "link_pvalue": link_pvalue, "link_color": link_color}

                    for col in nodeDataList:
                        child_dic[col] = list(nodeData[nodeData.Name.isin([child_name])][col])[0]

                    d['children'][key_list.index(parent_index)]['children'].append(child_dic)

        flare = d

        return flare

    def __df_to_Json(self, nodes, edges):

        flare = self.__df_to_flareJson(nodes, edges);

        nodeList = list(nodes.columns)

        if "Idx" in nodeList:
            nodeList.remove('Idx')

        if "Label" in nodeList:
            nodeList.remove('Label')

        if "color" in nodeList:
            nodeList.remove('color')

        if "block" in nodeList:
            nodeList.remove('block')

        nodeData = nodes[nodeList]
        nodeDataList = list(nodeData.drop(columns=['Name']).columns)

        flareString = ""

        bundleJsonArray = []
        completeChildList = []

        for key, value in flare.items():

            if isinstance(value, str):
                flareString = value
            elif isinstance(value, list):

                for idx, val in enumerate(value):

                    if "start_block" in edges.columns:
                        dParent = {"id": "", "Name": "", "Label": "", "node_color": "", "block": ""}

                        for col in nodeDataList:
                            dParent[col] = ""

                        dParent["imports"] = {}

                        parent_index = str(value[idx]['id'])
                        parentBlock = str(value[idx]['block'])

                        flareParentIndex = flareString + "#" + parentBlock + "#" + parent_index

                        dParent["block"] = parentBlock

                    else:
                        parent_index = str(value[idx]['id'])

                        dParent = {"id": "", "Name": "", "Label": "", "node_color": ""}

                        for col in nodeDataList:
                            dParent[col] = ""

                        dParent["imports"] = {}

                        flareParentIndex = flareString + "#" + parent_index

                    parentName = str(value[idx]['Name'])
                    parentLabel = str(value[idx]['Label'])
                    parentColor = str(value[idx]['node_color'])

                    dParent["id"] = flareParentIndex
                    dParent["Name"] = parentName
                    dParent["Label"] = parentLabel
                    dParent["node_color"] = parentColor

                    for col in nodeDataList:
                        dParent[col] = str(value[idx][col])

                    childList = value[idx]['children']

                    for child in childList:
                        link_score = float(child['link_score'])
                        link_sign = float(child['link_sign'])
                        link_pvalue = float(child['link_pvalue'])
                        link_color = str(child['link_color'])

                        if "start_block" in edges.columns:
                            dChild = {"id": "", "Name": "", "Label": "", "node_color": "", "block": ""}

                            for col in nodeDataList:
                                dChild[col] = ""

                            dChild["imports"] = {}

                            child_index = str(child['id'])
                            childBlock = str(child['block'])

                            flareChildIndex = flareString + "#" + childBlock + "#" + child_index

                            dChild["block"] = childBlock

                        else:
                            child_index = str(child['id'])
                            dChild = {"id": "", "Name": "", "Label": "", "node_color": ""}

                            for col in nodeDataList:
                                dChild[col] = ""

                            dChild["imports"] = {}

                            flareChildIndex = flareString + "#" + child_index

                        childName = str(child['Name'])
                        childLabel = str(child['Label'])
                        childColor = str(child['node_color'])

                        dParent["imports"][flareChildIndex] = {"link_score": link_score, "link_sign": link_sign, "link_pvalue": link_pvalue, "link_color": link_color}

                        dChild["id"] = flareChildIndex
                        dChild["Name"] = childName
                        dChild["Label"] = childLabel
                        dChild["node_color"] = childColor

                        for col in nodeDataList:
                            dChild[col] = str(child[col])

                        dChild["imports"][flareParentIndex] = {"link_score": link_score, "link_sign": link_sign, "link_pvalue": link_pvalue, "link_color": link_color}

                        completeChildList.append(dChild)

                    bundleJsonArray.append(dParent)
        bundleJsonArray.extend(completeChildList)

        return bundleJsonArray;

    def __get_colors(self, colorScale, x, cmap):
        scaled_colors = scaleData(x, colorScale, 0, 1)

        return cmap(scaled_colors)

    def __node_color(self, nodes, edges):

        colorsHEX = []
        nodeCmap = plt.cm.get_cmap(self.__node_cmap)

        if self.__node_color_column == 'none':
            nodes["color"] = "#000000"
        else:

            node_color_values = nodes[self.__node_color_column].values

            try:
                float(node_color_values[0])

                node_color_values = np.array([float(i) for i in node_color_values])

                colorsRGB = self.__get_colors(self.__nodeColorScale, node_color_values, nodeCmap)[:, :3]

                for rgb in colorsRGB:
                    colorsHEX.append(matplotlib.colors.rgb2hex(rgb))

                nodes["color"] = colorsHEX
            except ValueError:
                if matplotlib.colors.is_color_like(node_color_values[0]):
                    nodes["color"] = node_color_values
                else:
                    if self.__nodeColorScale != "ordinal":
                        print("Error: Node colour column is not valid. While colorScale is not ordinal, choose a column containing colour values, floats or integer values.")
                        sys.exit()
                    else:
                        colorsRGB = self.__get_colors(self.__nodeColorScale, node_color_values, nodeCmap)[:, :3]

                        for rgb in colorsRGB:
                            colorsHEX.append(matplotlib.colors.rgb2hex(rgb))

                        nodes["color"] = colorsHEX

        node_color = nodes['color'].reset_index().rename(columns={"index": "start_index"})

        edges = pd.merge(edges, node_color, how='left', on='start_index').rename(columns={"color": "start_color"})

        node_color = node_color.rename(columns={"start_index": "end_index"})

        edges = pd.merge(edges, node_color, how='left', on='end_index').rename(columns={"color": "end_color"})

        return nodes, edges

    def __edge_color(self, edges):

        colorsHEX = []
        edgeCmap = plt.cm.get_cmap(self.__edge_cmap)  # Sets the color palette for the edges

        signs = edges['sign'].values

        if "pvalue" in edges.columns:
            if "start_block" in edges.columns:
                edges_color = edges[['start_index', 'start_name', 'start_color', 'start_label', 'start_block', 'end_index', 'end_name', 'end_color', 'end_label', 'end_block', 'score', 'sign', 'pvalue']]
            else:
                edges_color = edges[['start_index', 'start_name', 'start_color', 'start_label', 'end_index', 'end_name', 'end_color', 'end_label', 'score', 'sign', 'pvalue']]
        else:

            if "start_block" in edges.columns:
                edges_color = edges[['start_index', 'start_name', 'start_color', 'start_label', 'start_block', 'end_index', 'end_name', 'end_color', 'end_label', 'end_block', 'score', 'sign']]
            else:
                edges_color = edges[['start_index', 'start_name', 'start_color', 'start_label', 'end_index', 'end_name', 'end_color', 'end_label', 'score', 'sign']]

        if self.__edge_color_value.lower() == "score":

            for i in range(edgeCmap.N):
                colorsHEX.append(matplotlib.colors.rgb2hex(edgeCmap(i)[:3]))

            signColors = []
            for sign in signs:
                if sign > 0:
                    signColors.append(colorsHEX[-1])
                else:
                    signColors.append(colorsHEX[0])

            edges_color = edges_color.assign(color=pd.Series(signColors, index=edges_color.index))
        elif self.__edge_color_value.lower() == "pvalue":

            if "pvalue" in edges_color.columns:
                colorsRGB = self.__get_colors(self.__edgeColorScale, edges_color['pvalue'].values, edgeCmap)[:, :3]

                for rgb in colorsRGB:
                    colorsHEX.append(matplotlib.colors.rgb2hex(rgb))

                edges_color = edges_color.assign(color=pd.Series(colorsHEX, index=edges_color.index))

            else:
                print("Pvalue in not a column in this dataset. Now choosing score as a color scale.")

                for i in range(edgeCmap.N):
                    colorsHEX.append(matplotlib.colors.rgb2hex(edgeCmap(i)[:3]))

                signColors = []
                for sign in signs:
                    if sign > 0:
                        signColors.append(colorsHEX[-1])
                    else:
                        signColors.append(colorsHEX[0])

                edges_color = edges_color.assign(color=pd.Series(signColors, index=edges_color.index))

        return edges_color

    def __getCSS(self):

        css_text = '''
        body {background-color: $backgroundColor;}
        
        .node {
            font: "Helvetica Neue", Helvetica, Arial, sans-serif;                            
        }
        
        .node:hover,
        .node--source,
        .node--target {
            stroke-opacity: 1.0;
            font-weight: bold;
            stroke-width: 4px;
        }        
    
        .link {
            stroke-opacity: 0.4;
            fill: none;
            pointer-events: none;
        }
        
        .link--source {
            stroke-opacity: 1.0;
            font-weight: 800;
            stroke-width: 4px;
        }
    
        .link--target {
            stroke-opacity: 1.0;            
        }
        
        #edgeBundlePanel {
            position: relative;
            width: 80%;
            height: 80%;
            margin: 0 auto;
            margin-top: auto;
            margin-bottom: auto;
            margin-left: auto;
            margin-right: auto;
        }
        
        #edgeBundle {
            margin-top: 50px;
        }
        
        .row {
            padding-left: 15px;
        }  
        
        #filterType {
            display: inline-block;
            position: relative;
            top: 0px;
            left: 0px; 
            color: $foregroundColor;
        }
        
        #scoreSelect {
            display: inline-block;
            position: absolute;
            top: 30px;
            left: 15px;
            color: $foregroundColor;
        }
        
        #abs_slider,
        #pos_slider,
        #neg_slider,
        #pvalue_slider,
        #tension_slider {
            position: relative;
            top: 35px;
        }
       
        #scoreSelect {
            display: block;
        }
        
        #save {
            position: relative;
            top: 3em;
            left: 0px;
            color: $foregroundColor;
        }
        
        .abs_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .pos_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .neg_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .pvalue_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .tension_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .abs_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto;
            /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .pos_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto;
            /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
         
        .neg_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto;
            /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .pvalue_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto;
            /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .tension_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto;
            /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .abs_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .pos_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .neg_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .pvalue_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .tension_slider.rzslider .rz-pointer:after {
            display: none;
        }
                
        h3, text {
            font-family: sans-serif;
                -webkit-touch-callout: none; /* iOS Safari */
                -webkit-user-select: none; /* Safari */
                -khtml-user-select: none; /* Konqueror HTML */
                -moz-user-select: none; /* Firefox */
                -ms-user-select: none; /* Internet Explorer/Edge */
                user-select: none; /* Non-prefixed version, currently supported by Chrome and Opera */
        } 
        '''

        return css_text

    def __getCSSdashboard(self):

        css_text = '''
        body {background-color: $backgroundColor;}
        
        .node {
            font: "Helvetica Neue", Helvetica, Arial, sans-serif;            
        }
        
        .node:hover,   
        .node--source,
        .node--target {
            stroke-opacity: 1.0;
            font-weight: 800;
            stroke-width: 4px;
        }

        .link {
            stroke-opacity: 0.4;
            fill: none;
        }
        
        .link--source {
            stroke-opacity: 1.0;
            font-weight: 800; 
            stroke-width: 4px;
        }
        
        .link--target {
            stroke-opacity: 1.0;
        }
        
        #edgeBundlePanel {
            position: relative;
            width: 65%;
            height: 65%;
            margin: 0 auto;
            margin-top: auto;
            margin-bottom: auto;
            margin-left: auto;
            margin-right: auto;
        }
        
        #filterType {
            display: inline-block;
            position: relative;
            top: 0px;
            left: 0px; 
            color: $foregroundColor;
        }
        
        #scoreSelect {
            display: inline-block;
            position: absolute;
            top: 42px;
            left: 5px;
            color: $foregroundColor;
        }
        
        #abs_slider, #pos_slider, #neg_slider, #pvalue_slider, #tension_slider {
            position: relative;
            top: 45px;
        }
        
        #scoreSelect {
            display: block;
        }
        
        #save {
            position: relative;
            top: 3em;
            left: 0px;
            color: $foregroundColor;
        }
        
        .abs_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
         
        .pos_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .neg_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .pvalue_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }
        
        .tension_slider.rzslider .rz-bar {
            background: #D3D3D3;
            height: 2px;
        }

        .abs_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto; /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .pos_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto; /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .neg_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto; /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
  
        .pvalue_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto; /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .tension_slider.rzslider .rz-pointer {
            width: 8px;
            height: 20px;
            top: auto; /* to remove the default positioning */
            bottom: 0;
            background-color: #333;
            border-top-left-radius: 3px;
            border-top-right-radius: 3px;
        }
        
        .abs_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .pos_slider.rzslider .rz-pointer:after {
            display: none;
        }
  
        .neg_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .pvalue_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        .tension_slider.rzslider .rz-pointer:after {
            display: none;
        }
        
        h3, text {
            font-family: sans-serif;
            -webkit-touch-callout: none; /* iOS Safari */
            -webkit-user-select: none; /* Safari */
            -khtml-user-select: none; /* Konqueror HTML */
            -moz-user-select: none; /* Firefox */
            -ms-user-select: none; /* Internet Explorer/Edge */
            user-select: none; /* Non-prefixed version, currently supported by Chrome and Opera */
        }
        
        td:nth-child(odd) {
            background-color: #eee;
            font-weight: bold;
        }
        '''

        return css_text

    def __getJS(self):

        js_text = '''
        
        var flareData = $flareData
        
        var pvalues = [];
        var p_scores = [];
        var n_scores = [];
        var abs_scores = [];
        
        var canvas = document.getElementById("edgeBundlePanel");
        var edgeBundle = d3.select(canvas).append("svg").attr("id", "edgeBundle");
        
        var redrawCount = 0;
        var prevRedrawCount = 0;
        
        var app = angular.module('rzSliderDemo', ['rzSlider']);
        
        function redraw(){
        
            if (redrawCount !== prevRedrawCount) {
                setTimeout(function(){
                    window.location.reload();
                });
                window.location.reload(); 
            }
            
            prevRedrawCount = redrawCount;
            
            redrawCount = redrawCount+1;
	        
	        var diameter = canvas.clientWidth;
            canvas.style.height = diameter;
                                            
            var radius = diameter / 2;
            var innerRadius = radius - $innerRadiusOffset;        
        
            var cluster = d3.cluster()
                        .separation(function(a, b) { return (a.parent == b.parent ? 1 : $blockSeparation ) })
                        .size([360, innerRadius]);
        
            edgeBundle.selectAll("*").remove();
        
            edgeBundle = d3.select("svg#edgeBundle")
    	                        .attr("width", diameter)
    	                        .attr("height", diameter)
                                .append("g")
    	                        .attr("transform", "translate(" + radius + "," + radius + ")")
                                .append("g");
        
            var node = edgeBundle.selectAll(".node");
            var link = edgeBundle.selectAll(".link");
            
            var linkLine = updateBundle(flareData);    //Initial generation of bundle to populate arrays
                                
            var currValues = {'abs_score': 0               
                        , 'p_score': 0                
                        , 'n_score': 0                
                        , 'pvalue': 1                
                        , 'tension': 0.85};
        
            
            
            String.prototype.trimLeft = function(charlist) {
                if (charlist === undefined)
                    charlist = "\s";

                return this.replace(new RegExp("^[" + charlist + "]+"), "");
            };
            
            Number.prototype.countDecimals = function () {
                if(Math.floor(this.valueOf()) === this.valueOf()) return 0;
                  
                var value = 0;
                var check = this.toString().includes("e-");
                
                if (check) {
                
                    var value = this.toString().split("-")[1];
                     
                } else {
                
                    var value1 = this.toString().split(".")[1];
                    var value2 = value1.trimLeft("0");
                    
                    var value = value1.length - value2.length + 1;
                }
                
                return value
            }
            
            app.controller('MainCtrl', function ($$scope, $$timeout) {
            
                $$scope.pos_visible = false;
                $$scope.neg_visible = false;
                $$scope.abs_visible = true;
                $$scope.pvalue_visible = false;
      
                $$scope.pos_toggle = function () {
                    if (!$$scope.pos_visible){
                        $$scope.pos_visible = !$$scope.pos_visible;
                        $$scope.abs_visible = false;
                        $$scope.neg_visible = false;
                        $$scope.pvalue_visible = false;
                        
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                    
                $$scope.neg_toggle = function () {
                    if (!$$scope.neg_visible){
                        $$scope.neg_visible = !$$scope.neg_visible;
                        $$scope.pos_visible = false;
                        $$scope.abs_visible = false;
                        $$scope.pvalue_visible = false;
                        
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                    
                $$scope.abs_toggle = function () {
                    if (!$$scope.abs_visible){  
                        $$scope.abs_visible = !$$scope.abs_visible;
                        $$scope.pos_visible = false;
                        $$scope.neg_visible = false;
                        $$scope.pvalue_visible = false;
                          
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                  
                $$scope.pvalue_toggle = function () {
                    if (!$$scope.pvalue_visible){  
                        $$scope.pvalue_visible = !$$scope.pvalue_visible;
                        $$scope.pos_visible = false;
                        $$scope.neg_visible = false;
                        $$scope.abs_visible = false;
                          
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                
                $$scope.score_toggle = function () {
                    $$scope.pvalue_visible = !$$scope.pvalue_visible;
                    
  			        var form = document.getElementById("scoreSelect")
  			        var form_val;
                    
                    for(var i=0; i<form.length; i++) {
        	            if(form[i].checked){
    				        form_val = form[i].id;        
    			        }
  			        }
                    
  			        if (form_val == "PosScoreRadio") { 
						$$scope.pos_visible = true;
  			        } else if (form_val == "NegScoreRadio") {
  					    $$scope.neg_visible = true;
  			        } else if (form_val == "AbsScoreRadio") {
 				 		$$scope.abs_visible = true;
				    }
                    
                    $$timeout(function () {
        		        $$scope.$$broadcast('rzSliderForceRender');
                    });
                };
                
                $$scope.abs_slider = {       
                        value: Number(d3.min(abs_scores).toFixed(4)),                        
                        options: {
                                showSelectionBar: true,                    
                                floor: Number(d3.min(abs_scores).toFixed(4)),
                                ceil: Number(d3.max(abs_scores).toFixed(4)),                          		
                                step: 0.01,
                                precision: 4,                                
                                getSelectionBarColor: function() { return '#2AE02A'; },
                                getPointerColor: function() { return '#D3D3D3'; },
                                pointerSize: 1,
                                onChange: function () {
                
                                            var absScoreValue = $$scope.abs_slider.value
                                            
                                            var tension = currValues.tension;
                                            currValues['abs_score'] = absScoreValue;
                                            
                                            //Filter all links out and update links
                                            var FlareData = filterData(2, 'score_abs');
                                                        
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                            
                                            //Apply new filter and update links
                                            var FlareData = filterData(absScoreValue, 'score_abs');
                                                        
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                }
                        }
                };
                
                if (p_scores.length != 0) {
                
                    $$scope.pos_slider = {       
                            value: Number(d3.min(p_scores).toFixed(4)),                        
                            options: {
                                    showSelectionBar: true,                    
                                    floor: Number(d3.min(p_scores).toFixed(4)),
                                    ceil: Number(d3.max(p_scores).toFixed(4)),                          		
                                    step: 0.01,
                                    precision: 4,                                    
                                    getSelectionBarColor: function() { return '#2AE02A'; },
                                    getPointerColor: function() { return '#D3D3D3'; },
                                    pointerSize: 1,
                                    onChange: function () {
                
                                            var pScoreValue = $$scope.pos_slider.value
                                            
                                            var tension = currValues.tension;
                                            currValues['p_score'] = pScoreValue;
                                            
                                            //Filter all links out and update links
                                            var FlareData = filterData(2, 'score_pos');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                            
                                            //Apply new filter and update links
                                            var FlareData = filterData(pScoreValue, 'score_pos');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                    }
                            }
                    };
                }
                
                if (n_scores.length != 0) {               
                        
                    $$scope.neg_slider = {       
                            value: Number(d3.max(n_scores).toFixed(4)),                        
                            options: {
                                    showSelectionBar: true,                    
                                    floor: Number(d3.min(n_scores).toFixed(4)),
                                    ceil: Number(d3.max(n_scores).toFixed(4)),                          		
                                    step: 0.01,
                                    precision: 4,                                    
                                    getSelectionBarColor: function() { return '#2AE02A'; },
                                    getPointerColor: function() { return '#D3D3D3'; },
                                    pointerSize: 1,
                                    onChange: function () {
                
                                            var nScoreValue = $$scope.neg_slider.value
                                            
                                            var tension = currValues.tension;
                                            currValues['n_score'] = nScoreValue;
                                            
                                            //Filter all links out and update links
                                            var FlareData = filterData(-2, 'score_neg');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                            
                                            //Apply new filter and update links
                                            var FlareData = filterData(nScoreValue, 'score_neg');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                    }
                            }
                    };
                }
                
                if (pvalues.length != 0) {
                                                
                    $$scope.pvalue_slider = {       
                                    value: Number(d3.max(pvalues).toFixed(Number(d3.min(pvalues).countDecimals()))),                       
                                    options: {
                                            showSelectionBar: true,     
                                            floor: Number(d3.min(pvalues).toFixed(Number(d3.min(pvalues).countDecimals()))),
                                            ceil: Number(d3.max(pvalues).toFixed(Number(d3.min(pvalues).countDecimals()))),
                                            step: Number(d3.min(pvalues).toFixed(Number(d3.min(pvalues)).countDecimals())),
                                            precision: Number(d3.min(pvalues).countDecimals()),                                            
                                            getSelectionBarColor: function() { return '#2AE02A'; },
                                            getPointerColor: function() { return '#D3D3D3'; },
                                            pointerSize: 1,
                                            onChange: function () {
                                      
                                                        var pvalueValue = $$scope.pvalue_slider.value;
                                                        var tension = currValues.tension;
                                                        currValues['pvalue'] = pvalueValue;
                                       
                                                        //Filter all links out and update links
                                                        var FlareData = filterData(Number(d3.min(pvalues))/10, 'pvalue');
                                                    
                                                        var linkLine = updateBundle(FlareData);
                                                    
                                                        var line = linkLine.line;
                                                        var link = linkLine.link;
                                    
                                                        line.curve(d3.curveBundle.beta(tension));
                                                        link.attr("d", d => line(d.source.path(d.target)));
                                                        
                                                        //Apply new filter and update links
                                                        var FlareData = filterData(pvalueValue, 'pvalue');
                                                    
                                                        var linkLine = updateBundle(FlareData);
                                                    
                                                        var line = linkLine.line;
                                                        var link = linkLine.link;
                                    
                                                        line.curve(d3.curveBundle.beta(tension));
                                                        link.attr("d", d => line(d.source.path(d.target)));
                                                        
                                            }
                                    }
                    };
                }
        
                $$scope.tension_slider = {       
                                value: Number(0.85),                        
                                options: {
                                        showSelectionBar: true,                    
                                        floor: Number(0.0),
                                        ceil: Number(1.0),
                                        step: 0.05,
                                        precision: 4,                                        
                                        getSelectionBarColor: function() { return '#2AE02A'; },
                                        getPointerColor: function() { return '#D3D3D3'; },
                                        pointerSize: 1,
                                        onChange: function () {
                
                                                    var tension =  $$scope.tension_slider.value
                            
                                                    currValues['tension'] = tension;
                                                
                                                    var form = document.getElementById("filterType")
                                                    var form_val;
                                                    
                                                    for(var i=0; i<form.length; i++) {
                                                        if(form[i].checked) {
                                                            form_val = form[i].id;        
                                                        }
                                                    }
                                                                
                                                    if (form_val == "scoreRadio") { 
                                                                
                                                        var score_form = document.getElementById("scoreSelect")
                                                        var score_form_val;
                                                        
                                                        for(var i=0; i<score_form.length; i++){
                                                            if(score_form[i].checked){
                                                                score_form_val = score_form[i].id;        
                                                            }
                                                        }
                                                                    
                                                        if (score_form_val == "PosScoreRadio") {
                                                            var p_scoreValue = currValues.p_score;
                                                            var FlareData = filterData(p_scoreValue, 'score_pos');
                                                        } else if (score_form_val == "NegScoreRadio") {
                                                            var n_scoreValue = currValues.n_score;
                                                            var FlareData = filterData(n_scoreValue, 'score_neg');
                                                        } else if (score_form_val == "AbsScoreRadio") {
                                                            var abs_scoreValue = currValues.abs_score;
                                                            var FlareData = filterData(abs_scoreValue, 'score_abs');
                                                        }
                                                    } else if (form_val == "pvalueRadio") {
                                                        var pvalueValue = currValues.pvalue;
                                                        var FlareData = filterData(pvalueValue, 'pvalue');
                                                    }
                    
                                                    var linkLine = updateBundle(FlareData);
          
                                                    var line = linkLine.line;
                                                    var link = linkLine.link;
                                                                
                                                    line.curve(d3.curveBundle.beta(tension));
                                                    link.attr("d", d => line(d.source.path(d.target)));     
                                      
                                        }
                                }
                };
    
                $$scope.savebutton = function () {
                                                
                                var options = {
                                        canvg: window.canvg,
                                        backgroundColor: '$backgroundColor',
                                        height: diameter+100,
                                        width: diameter+100,
                                        left: -50,
                                        top: -50,                                        
                                        scale: 2/window.devicePixelRatio,
                                        encoderOptions: 1,
                                        ignoreMouse : true,
                                        ignoreAnimation : true,
                                }
                                                   
                                saveSvgAsPng(d3.select('svg#edgeBundle').node(), "edgeBundle.png", options);
                }       
            });
            
            function changeFilter() {
                
                var form = document.getElementById("filterType")
                var form_val;
                
                for(var i=0; i<form.length; i++){
                    if(form[i].checked){
                        form_val = form[i].id;        
                    }
                }
          
                if (form_val == "scoreRadio") { 
                    d3.select('#scoreSelect').style("display", 'block');
                    
                    var form_score = document.getElementById("scoreSelect")
                    var form_val_score;
                    
                    for(var i=0; i<form_score.length; i++){
                        if(form_score[i].checked){
                            form_val_score = form_score[i].id;        
                        }
                    }
                    
                    if (form_val_score == "PosScoreRadio") {
                        //Filter out all links prior to updating with the score threshold
                        var FlareData = filterData(1, 'score_pos');    
                        var linkLine = updateBundle(FlareData);
                        
                        //Filter with the new score threshold
                        var FlareData = filterData(currValues.p_score, 'score_pos');        
                        var linkLine = updateBundle(FlareData);
                    } else if (form_val_score == "NegScoreRadio") {   
                        //Filter out all links prior to updating with the score threshold
                        var FlareData = filterData(-1, 'score_neg');    
                        var linkLine = updateBundle(FlareData);
                                        
                        //Filter with the new score threshold
                        var FlareData = filterData(currValues.n_score, 'score_neg');  
                        var linkLine = updateBundle(FlareData);       
                    } else if (form_val_score == "AbsScoreRadio") {
                        //Filter out all links prior to updating with the score threshold
                        var FlareData = filterData(1, 'score_abs');    
                        var linkLine = updateBundle(FlareData);
                                        
                        //Filter with the new score threshold
                        var FlareData = filterData(currValues.abs_score, 'score_abs');
                        var linkLine = updateBundle(FlareData);
                    }
                } else if (form_val == "pvalueRadio") {
                    d3.select('#scoreSelect').style("display", 'none');
                    
                    //Filter out all links prior to updating with the pvalue threshold
                    var FlareData = filterData(-1, 'pvalue');    
                    var linkLine = updateBundle(FlareData);
                    
                    //Filter with the new pvalue threshold                    
                    var FlareData = filterData(currValues.pvalue, 'pvalue');
                    var linkLine = updateBundle(FlareData);
                }
          
                var tension = currValues.tension;
                
                var line = linkLine.line;
                var link = linkLine.link;
                
                line.curve(d3.curveBundle.beta(tension));
                link.attr("d", d => line(d.source.path(d.target)));
            }
        
            function changeScore() {
                
                var form = document.getElementById("scoreSelect")
                var form_val;
                
                for(var i=0; i<form.length; i++) {
                    if(form[i].checked){
                        form_val = form[i].id;        
                    }
                }
                
                if (form_val == "PosScoreRadio") {
                    //Filter out all links prior to updating with the score threshold
                    var FlareData = filterData(1, 'score_pos');
                    var linkLine = updateBundle(FlareData);
                    
                    var FlareData = filterData(currValues.p_score, 'score_pos');        
                    var linkLine = updateBundle(FlareData);
                } else if (form_val == "NegScoreRadio") {                    
                    //Filter out all links prior to updating with the score threshold
                    var FlareData = filterData(-1, 'score_neg');    
                    var linkLine = updateBundle(FlareData);              
                    
                    var FlareData = filterData(currValues.n_score, 'score_neg');  
                    var linkLine = updateBundle(FlareData);        
                } else if (form_val == "AbsScoreRadio") {
                    //Filter out all links prior to updating with the score threshold
                    var FlareData = filterData(1, 'score_abs');
                    var linkLine = updateBundle(FlareData);
                    
                    var FlareData = filterData(currValues.abs_score, 'score_abs');
                    var linkLine = updateBundle(FlareData);
                }
                
                var tension = currValues.tension;
                      
                var line = linkLine.line;
                var link = linkLine.link;
                      
                line.curve(d3.curveBundle.beta(tension));
                link.attr("d", d => line(d.source.path(d.target)));
            }
        
            var filterDim = d3.select("#filterType");
            filterDim.on("change", changeFilter);
            
            var selectDim = d3.select("#scoreSelect");
            selectDim.on("change", changeScore);
            
            function updateBundle(data) {
                
                pvalues = []
                p_scores = []
                n_scores = []
                abs_scores = []
                
                var line = d3.radialLine()
                    .curve(d3.curveBundle.beta(0.85))
                    .radius(function(d) { return d.y; })
                    .angle(function(d) { return d.x / 180 * Math.PI; });
                
                var root = d3.hierarchy(packageHierarchy(data), (d) => d.children);
                
                cluster(root)
                
                var nodes = root.descendants();
                  
                node = node.data(nodes.filter(function(n) { return !n.children; }));
                
                node.exit().remove();
                
                var fontBase = 1000;
                var fontSize = $fontSize;
                
                function getFont() {
                    var ratio = fontSize / fontBase;
                    var width = canvas.clientWidth;                    
                    var size = width * ratio;
                                                        
                    return (size|0) + 'px';  
                }
                
                if ("$mouseOver" == "true") {
                
                    var newNode = node.enter().append("text")
                                        .attr("class", "node")
                                        .attr("dy", ".31em")
                                        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 8) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
                                        .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
                                        .text(function(d) { return d.data.Label; })
                                        .style("font-size", getFont())
                                        .style("fill", function(d) { return d.data.node_color; })
                                        .on("mouseover", mouseovered)
                                        .on("mouseout", mouseouted);
                } else {
                
                    var newNode = node.enter().append("text")
                                        .attr("class", "node")
                                        .attr("dy", ".31em")
                                        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 8) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
                                        .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
                                        .text(function(d) { return d.data.Label; })
                                        .style("font-size", getFont())
                                        .style("fill", function(d) { return d.data.node_color; })
                                        .on("click", mouseovered)
                                        .on("dblclick", mouseouted);
                }                   
                
                node = node.merge(newNode);
                
                var links = packageImports(root.descendants());
                
                links = links.map(d=> ({ ...d
                                        , link_color: d.source.data.imports[d.target.data.id]["link_color"]
                                        , link_score: d.source.data.imports[d.target.data.id]["link_score"]
                                        , link_pvalue : d.source.data.imports[d.target.data.id]["link_pvalue"]}));
                
                links.forEach(function(d) { abs_scores.push(Math.abs(d.link_score))
                                            , pvalues.push(d.link_pvalue);
                                        
                                            if (d.link_score >= 0) {
                                        
                                                p_scores.push(d.link_score);
                                         
                                            } else {
                                    
                                                n_scores.push(d.link_score);
                                      
                                            }
                            });
                
                link = link.data(links);
                
                link.exit().remove();
                  
                var newLink = link.enter().append("path")
                                .attr("class", "link")
                                .attr('d', d => line(d.source.path(d.target)))
                                .style("stroke", function(d) { return d.link_color; });
                
                link = link.merge(newLink);
                
                var linkLine = {"line": line, "link": link}            
                
                function mouseovered(d) {
                            
                    node
                        .each(function(n) { n.target = n.source = false; });
                    
                    link
                        .classed("link--target", function(l) { if (l.target === d) return l.source.source = true; })
                        .classed("link--source", function(l) { if (l.source === d) return l.target.target = true; })
                        .filter(function(l) { return l.target === d || l.source === d; })
                        .each(function() { this.parentNode.appendChild(this); })
                    
                    node
                        .classed("node--both", function(n) { return n.source && n.target; })
                        .classed("node--target", function(n) { return n.target; })
                        .classed("node--source", function(n) { return n.source; });
                                    
                    link.style('opacity', o => (o.source === d || o.target === d ? 1 : $linkFadeOpacity))
                }
                
                function mouseouted(d) {
                
                    link
                        .classed("link--target", false)
                        .classed("link--source", false);
                    
                    node
                        .classed("node--both", false)
                        .classed("node--target", false)
                        .classed("node--source", false);
                            
                    link.style('opacity', 1);
                    node.style('opacity', 1);                    
                }
                
                function packageHierarchy(classes) {
                    var map = {};
                    
                    function find(id, data) {
                        var node = map[id], i;
                        if (!node) {
                            node = map[id] = data || {id: id, children: []};
                            if (id.length) {
                                node.parent = find(id.substring(0, i = id.lastIndexOf("#")));
                                node.parent.children.push(node);
                                node.key = id.substring(i + 1);
                            }
                        }
                        return node;
                    }
                    
                    classes.forEach(function(d) {
                        find(d.id, d);
                    });
                    
                    return map[""];
                }
                
                function packageImports(nodes) {
                    var map = {}, imports = [];
                    
                    nodes.forEach(function(d) {
                        map[d.data.id] = d;
                    });
                    
                    nodes.forEach(function(d) {
                        if (d.data.imports) Object.keys(d.data.imports).forEach(function(i) {    
                            imports.push({source: map[d.data.id], target: map[i]});
                        });
                    });
                    
                    return imports;
                }
                
                return linkLine;
            }
            
            function filterData(threshold, filtType) {
                
                const data = flareData.map(a => ({...a}));
                            
                var FlareData = []
                
                //Remove nodes from imports with weight below threshold
                for (var i = 0; i < data.length; i++) {
                    var flare = data[i];
                    
                    var links = flare.imports;
                    var newLinks = {}
                    
                    for (const [key, value] of Object.entries(links)) {
                        
                        var link_score = value["link_score"];
                        var link_pvalue = value["link_pvalue"];
                        var link_color = value["link_color"];
                        
                        if (filtType == 'score_abs') {
                            
                            if (Math.abs(link_score) >= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }
                                
                        } else if (filtType == 'score_neg') {
                            
                            if (link_score <= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }
                            
                        } else if (filtType == 'score_pos') {
                            if (link_score >= threshold) {
                                newLinks[key] = {"link_score": link_score
                                               , "link_pvalue": link_pvalue
                                               , "link_color": link_color};
                            }
                                                
                        } else if (filtType == 'pvalue') {
                            if (link_pvalue <= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }
                        }
                    }
                
                    flare.imports = newLinks;
                    
                    FlareData.push(flare)
                }
            
                return FlareData;
            }
        }
        
        redraw();
        
        window.addEventListener("resize", redraw);        
        '''

        return js_text

    def __getJSdashboard(self):

        js_text = '''
        
        var flareData = $flareData
        
        var pvalues = [];
        var p_scores = [];
        var n_scores = [];
        var abs_scores = [];

        var canvas = document.getElementById("edgeBundlePanel");
        var edgeBundle = d3.select(canvas).append("svg").attr("id", "edgeBundle");
        
        var redrawCount = 0;
        var prevRedrawCount = 0;
        
        var app = angular.module('rzSliderDemo', ['rzSlider']);
        
        function redraw(){

            if (redrawCount !== prevRedrawCount) {
                    
  	            setTimeout(function(){
                    window.location.reload();
                });
                window.location.reload();
            }
            
            prevRedrawCount = redrawCount;

	        redrawCount = redrawCount+1;
            
            var diameter = canvas.clientWidth;
            canvas.style.height = diameter;
            
            var radius = diameter / 2;
            var innerRadius = radius - $innerRadiusOffset;
            
            var cluster = d3.cluster()
                        .separation(function(a, b) { return (a.parent == b.parent ? 1 : $blockSeparation ) })
                        .size([360, innerRadius]);
      
            edgeBundle.selectAll("*").remove();
            
            edgeBundle = d3.select("svg#edgeBundle")
          	        .attr("width", diameter)
    	            .attr("height", diameter)
                    .append("g")      
    	            .attr("transform", "translate(" + radius + "," + radius + ")")
                    .append("g");
        
	        var node = edgeBundle.selectAll(".node");
	        var link = edgeBundle.selectAll(".link");
	        
	        var linkLine = updateBundle(flareData); //Initial generation of bundle to populate arrays
	        
            var currValues = {'abs_score': 0               
                            , 'p_score': 0                
                            , 'n_score': 0                
                            , 'pvalue': 1                
                            , 'tension': 0.85};
            
            String.prototype.trimLeft = function(charlist) {
                if (charlist === undefined)
                    charlist = "\s";

                return this.replace(new RegExp("^[" + charlist + "]+"), "");
            };
        
            Number.prototype.countDecimals = function () {
                if(Math.floor(this.valueOf()) === this.valueOf()) return 0;
        
                var value = 0;
                var check = this.toString().includes("e-");
                
                if (check) {
                    
    	            var value = this.toString().split("-")[1];
                     
                } else {
    	            
                    var value1 = this.toString().split(".")[1];
                    var value2 = value1.trimLeft("0");
                     
                    var value = value1.length - value2.length + 1;
                }        
                
                return value
            }
            
            app.controller('MainCtrl', function ($$scope, $$timeout) {
                
                $$scope.pos_visible = false;
                $$scope.neg_visible = false;
                $$scope.abs_visible = true;
                $$scope.pvalue_visible = false;
      
                $$scope.pos_toggle = function () {
                    if (!$$scope.pos_visible){
                        $$scope.pos_visible = !$$scope.pos_visible;
                        $$scope.abs_visible = false;
                        $$scope.neg_visible = false;
                        $$scope.pvalue_visible = false;
            
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                
                $$scope.neg_toggle = function () {
                    if (!$$scope.neg_visible){
                        $$scope.neg_visible = !$$scope.neg_visible;
                        $$scope.pos_visible = false;
                        $$scope.abs_visible = false;
                        $$scope.pvalue_visible = false;
            
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                
                $$scope.abs_toggle = function () {
                   if (!$$scope.abs_visible){  
                        $$scope.abs_visible = !$$scope.abs_visible;
                        $$scope.pos_visible = false;
                        $$scope.neg_visible = false;
                        $$scope.pvalue_visible = false;
              
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
      
                $$scope.pvalue_toggle = function () {
                    if (!$$scope.pvalue_visible){  
                        $$scope.pvalue_visible = !$$scope.pvalue_visible;
                        $$scope.pos_visible = false;
                        $$scope.neg_visible = false;
                        $$scope.abs_visible = false;
              
                        $$timeout(function () {
                            $$scope.$$broadcast('rzSliderForceRender');
                        });
                    }
                };
                
                $$scope.score_toggle = function () {
                    $$scope.pvalue_visible = !$$scope.pvalue_visible;
                    
  			        var form = document.getElementById("scoreSelect")
  			        var form_val;
                    
                    for(var i=0; i<form.length; i++) {
        	            if(form[i].checked){
    				        form_val = form[i].id;        
    			        }
  			        }
                    
  			        if (form_val == "PosScoreRadio") { 
						$$scope.pos_visible = true;
  			        } else if (form_val == "NegScoreRadio") {
  					    $$scope.neg_visible = true;
  			        } else if (form_val == "AbsScoreRadio") {
 				 		$$scope.abs_visible = true;
				    }
                    
                    $$timeout(function () {
        		        $$scope.$$broadcast('rzSliderForceRender');
                    });
                };
                
                $$scope.abs_slider = {       
                        value: Number(d3.min(abs_scores).toFixed(4)),                        
                        options: {
                                showSelectionBar: true,                    
                                floor: Number(d3.min(abs_scores).toFixed(4)),
                                ceil: Number(d3.max(abs_scores).toFixed(4)),                          		
                                step: 0.01,
                                precision: 4,                                
                                getSelectionBarColor: function() { return '#2AE02A'; },
                                getPointerColor: function() { return '#D3D3D3'; },
                                pointerSize: 1,
                                onChange: function () {
                
                                            var absScoreValue = $$scope.abs_slider.value
                                            
                                            var tension = currValues.tension;
                                            currValues['abs_score'] = absScoreValue;
                                            
                                            //Filter all links out and update links
                                            var FlareData = filterData(2, 'score_abs');
                                                        
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                            
                                            //Apply new filter and update links
                                            var FlareData = filterData(absScoreValue, 'score_abs');
                                                        
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                }
                        }
                };
                
                if (p_scores.length != 0) {
                
                    $$scope.pos_slider = {       
                            value: Number(d3.min(p_scores).toFixed(4)),                        
                            options: {
                                    showSelectionBar: true,                    
                                    floor: Number(d3.min(p_scores).toFixed(4)),
                                    ceil: Number(d3.max(p_scores).toFixed(4)),                          		
                                    step: 0.01,
                                    precision: 4,                                    
                                    getSelectionBarColor: function() { return '#2AE02A'; },
                                    getPointerColor: function() { return '#D3D3D3'; },
                                    pointerSize: 1,
                                    onChange: function () {
                
                                            var pScoreValue = $$scope.pos_slider.value
                                            
                                            var tension = currValues.tension;
                                            currValues['p_score'] = pScoreValue;
                                            
                                            //Filter all links out and update links
                                            var FlareData = filterData(2, 'score_pos');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                            
                                            //Apply new filter and update links
                                            var FlareData = filterData(pScoreValue, 'score_pos');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                    }
                            }
                    };
                }
                
                if (n_scores.length != 0) {               
                        
                    $$scope.neg_slider = {       
                            value: Number(d3.max(n_scores).toFixed(4)),                        
                            options: {
                                    showSelectionBar: true,                    
                                    floor: Number(d3.min(n_scores).toFixed(4)),
                                    ceil: Number(d3.max(n_scores).toFixed(4)),                          		
                                    step: 0.01,
                                    precision: 4,                                    
                                    getSelectionBarColor: function() { return '#2AE02A'; },
                                    getPointerColor: function() { return '#D3D3D3'; },
                                    pointerSize: 1,
                                    onChange: function () {
                
                                            var nScoreValue = $$scope.neg_slider.value
                                            
                                            var tension = currValues.tension;
                                            currValues['n_score'] = nScoreValue;
                                            
                                            //Filter all links out and update links
                                            var FlareData = filterData(-2, 'score_neg');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                            
                                            //Apply new filter and update links
                                            var FlareData = filterData(nScoreValue, 'score_neg');
                                                                
                                            var linkLine = updateBundle(FlareData);
          
                                            var line = linkLine.line;
                                            var link = linkLine.link;
          
                                            line.curve(d3.curveBundle.beta(tension));
                                            link.attr('d', d => line(d.source.path(d.target)));
                                    }
                            }
                    };
                }
                
                if (pvalues.length != 0) {
                                                
                    $$scope.pvalue_slider = {       
                                    value: Number(d3.max(pvalues).toFixed(Number(d3.min(pvalues).countDecimals()))),                       
                                    options: {
                                            showSelectionBar: true,     
                                            floor: Number(d3.min(pvalues).toFixed(Number(d3.min(pvalues).countDecimals()))),
                                            ceil: Number(d3.max(pvalues).toFixed(Number(d3.min(pvalues).countDecimals()))),
                                            step: Number(d3.min(pvalues).toFixed(Number(d3.min(pvalues)).countDecimals())),
                                            precision: Number(d3.min(pvalues).countDecimals()),                                            
                                            getSelectionBarColor: function() { return '#2AE02A'; },
                                            getPointerColor: function() { return '#D3D3D3'; },
                                            pointerSize: 1,
                                            onChange: function () {
                                      
                                                        var pvalueValue = $$scope.pvalue_slider.value;
                                                        var tension = currValues.tension;
                                                        currValues['pvalue'] = pvalueValue;
                                       
                                                        //Filter all links out and update links
                                                        var FlareData = filterData(Number(d3.min(pvalues))/10, 'pvalue');
                                                    
                                                        var linkLine = updateBundle(FlareData);
                                                    
                                                        var line = linkLine.line;
                                                        var link = linkLine.link;
                                    
                                                        line.curve(d3.curveBundle.beta(tension));
                                                        link.attr("d", d => line(d.source.path(d.target)));
                                                        
                                                        //Apply new filter and update links
                                                        var FlareData = filterData(pvalueValue, 'pvalue');
                                                    
                                                        var linkLine = updateBundle(FlareData);
                                                    
                                                        var line = linkLine.line;
                                                        var link = linkLine.link;
                                    
                                                        line.curve(d3.curveBundle.beta(tension));
                                                        link.attr("d", d => line(d.source.path(d.target)));
                                            }
                                    }
                    };
                }
        
                $$scope.tension_slider = {       
                                value: Number(0.85),                        
                                options: {
                                        showSelectionBar: true,                    
                                        floor: Number(0.0),
                                        ceil: Number(1.0),
                                        step: 0.05,
                                        precision: 4,                                        
                                        getSelectionBarColor: function() { return '#2AE02A'; },
                                        getPointerColor: function() { return '#D3D3D3'; },
                                        pointerSize: 1,
                                        onChange: function () {
                
                                                    var tension =  $$scope.tension_slider.value
                            
                                                    currValues['tension'] = tension;
                                                
                                                    var form = document.getElementById("filterType")
                                                    var form_val;
                                                    
                                                    for(var i=0; i<form.length; i++) {
                                                        if(form[i].checked) {
                                                            form_val = form[i].id;        
                                                        }
                                                    }
                                                                
                                                    if (form_val == "scoreRadio") { 
                                                                
                                                        var score_form = document.getElementById("scoreSelect")
                                                        var score_form_val;
                                                        
                                                        for(var i=0; i<score_form.length; i++){
                                                            if(score_form[i].checked){
                                                                score_form_val = score_form[i].id;        
                                                            }
                                                        }
                                                                    
                                                        if (score_form_val == "PosScoreRadio") {
                                                            var p_scoreValue = currValues.p_score;
                                                            var FlareData = filterData(p_scoreValue, 'score_pos');
                                                        } else if (score_form_val == "NegScoreRadio") {
                                                            var n_scoreValue = currValues.n_score;
                                                            var FlareData = filterData(n_scoreValue, 'score_neg');
                                                        } else if (score_form_val == "AbsScoreRadio") {
                                                            var abs_scoreValue = currValues.abs_score;
                                                            var FlareData = filterData(abs_scoreValue, 'score_abs');
                                                        }
                                                    } else if (form_val == "pvalueRadio") {
                                                        var pvalueValue = currValues.pvalue;
                                                        var FlareData = filterData(pvalueValue, 'pvalue');
                                                    }
                    
                                                    var linkLine = updateBundle(FlareData);
          
                                                    var line = linkLine.line;
                                                    var link = linkLine.link;
                                                                
                                                    line.curve(d3.curveBundle.beta(tension));
                                                    link.attr("d", d => line(d.source.path(d.target)));     
                                      
                                        }
                                }
                };
    
                $$scope.savebutton = function () {
                                    
                          var options = {
                                    canvg: window.canvg,
                                    backgroundColor: '$backgroundColor',
                                    height: diameter+100,
                                    width: diameter+100,
                                    left: -50,
                                    top: -50,
                                    scale: 2/window.devicePixelRatio,
                                    encoderOptions: 1,
                                    ignoreMouse : true,
                                    ignoreAnimation : true,
                            }
                                                   
                            saveSvgAsPng(d3.select('svg#edgeBundle').node(), "edgeBundle.png", options);           					
                }       
            });
            
            function changeFilter() {
    
                var form = document.getElementById("filterType")
                var form_val;
          
                for(var i=0; i<form.length; i++){
                    if(form[i].checked){
                        form_val = form[i].id;        
                    }
                }
          
                if (form_val == "scoreRadio") {
                    d3.select('#scoreSelect').style("display", 'block');
                    
                    var form_score = document.getElementById("scoreSelect")
                    var form_val_score;
          
                    for(var i=0; i<form_score.length; i++){
                        if(form_score[i].checked){
                            form_val_score = form_score[i].id;        
                        }
                    }
          
                    if (form_val_score == "PosScoreRadio") {
                        
                        //Filter out all links prior to updating with the score threshold
                        var FlareData = filterData(1, 'score_pos');
                        var linkLine = updateBundle(FlareData);
                
                        var FlareData = filterData(currValues.p_score, 'score_pos');        
                        var linkLine = updateBundle(FlareData);
                    } else if (form_val_score == "NegScoreRadio") {
                        
                        var FlareData = filterData(-1, 'score_neg');    
                        var linkLine = updateBundle(FlareData);
                
                        var FlareData = filterData(currValues.n_score, 'score_neg');  
                        var linkLine = updateBundle(FlareData);       
                    } else if (form_val_score == "AbsScoreRadio") {
                        
                        //Filter out all links prior to updating with the score threshold
                        var FlareData = filterData(1, 'score_abs');
                        var linkLine = updateBundle(FlareData);
                        
                        var FlareData = filterData(currValues.abs_score, 'score_abs');
                        var linkLine = updateBundle(FlareData);
                    }
                } else if (form_val == "pvalueRadio") {
                    d3.select('#scoreSelect').style("display", 'none');
                    
                    //Filter out all links prior to updating with the pvalue threshold
                    var FlareData = filterData(-1, 'pvalue');
                    var linkLine = updateBundle(FlareData);
                    
                    var FlareData = filterData(currValues.pvalue, 'pvalue');
                    var linkLine = updateBundle(FlareData);
                }
          
                var tension = currValues.tension;
                
                var line = linkLine.line;
                var link = linkLine.link;
                
                line.curve(d3.curveBundle.beta(tension));
                link.attr("d", d => line(d.source.path(d.target)));
            }
    
            function changeScore() {
      
                var form = document.getElementById("scoreSelect")
                var form_val;
                
                for(var i=0; i<form.length; i++) {
                    if(form[i].checked){
                        form_val = form[i].id;        
                    }
                }
                
                if (form_val == "PosScoreRadio") { 
                    
                    //Filter out all links prior to updating with the score threshold
                    var FlareData = filterData(1, 'score_pos');
                    var linkLine = updateBundle(FlareData);
                    
                    var FlareData = filterData(currValues.p_score, 'score_pos');        
                    var linkLine = updateBundle(FlareData);      
                    
                } else if (form_val == "NegScoreRadio") {
                    
                    //Filter out all links prior to updating with the score threshold
                    var FlareData = filterData(-1, 'score_neg');    
                    var linkLine = updateBundle(FlareData);
                    
                    var FlareData = filterData(currValues.n_score, 'score_neg');  
                    var linkLine = updateBundle(FlareData);        
                } else if (form_val == "AbsScoreRadio") {
                    
                    //Filter out all links prior to updating with the score threshold
                    var FlareData = filterData(1, 'score_abs');
                    var linkLine = updateBundle(FlareData);
                    
                    var FlareData = filterData(currValues.abs_score, 'score_abs');
                    var linkLine = updateBundle(FlareData);
                }
                           
                var tension = currValues.tension;
                 
                var line = linkLine.line;
                var link = linkLine.link;
                   
                line.curve(d3.curveBundle.beta(tension));
                link.attr("d", d => line(d.source.path(d.target)));
            }
            
            var filterDim = d3.select("#filterType");
            filterDim.on("change", changeFilter);
            
            var selectDim = d3.select("#scoreSelect");
            selectDim.on("change", changeScore);
            
            function updateBundle(data) {
    
                pvalues = []
                p_scores = []
                n_scores = []
                abs_scores = []
    
                var line = d3.radialLine()
                        .curve(d3.curveBundle.beta(0.85))
                        .radius(function(d) { return d.y; })
                        .angle(function(d) { return d.x / 180 * Math.PI; });
                
                var root = d3.hierarchy(packageHierarchy(data), (d) => d.children);
                
                cluster(root)
                
                var nodes = root.descendants();
                
                node = node.data(nodes.filter(function(n) { return !n.children; }));
                
                node.exit().remove();
                
                var fontBase = 1000;
                var fontSize = $fontSize;
                
                function getFont() {
                    var ratio = fontSize / fontBase;
                    var width = canvas.clientWidth;                    
                    var size = width * ratio;
                                                        
                    return (size|0) + 'px';  
                }
                
                if ("$mouseOver" == "true") {
                
                    var newNode = node.enter().append("text")
                                        .attr("class", "node")
                                        .attr("dy", ".31em")
                                        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 8) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
                                        .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
                                        .text(function(d) { return d.data.Label; })
                                        .style("font-size", getFont())
                                        .style("fill", function(d) { return d.data.node_color; })
                                        .on("mouseover", mouseovered_node)
                                        .on("mouseout", mouseouted);
                } else {
                
                    var newNode = node.enter().append("text")
                                        .attr("class", "node")
                                        .attr("dy", ".31em")
                                        .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + (d.y + 8) + ",0)" + (d.x < 180 ? "" : "rotate(180)"); })
                                        .style("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
                                        .text(function(d) { return d.data.Label; })
                                        .style("font-size", getFont())
                                        .style("fill", function(d) { return d.data.node_color; })
                                        .on("click", mouseovered_node)
                                        .on("dblclick", mouseouted);
                }
                
                node = node.merge(newNode);
                
                var links = packageImports(root.descendants());
      
                links = links.map(d=> ({ ...d
                                        , link_color : d.source.data.imports[d.target.data.id]["link_color"]
                                        , link_score : d.source.data.imports[d.target.data.id]["link_score"]
                                        , link_pvalue : d.source.data.imports[d.target.data.id]["link_pvalue"]}));
                
                links.forEach(function(d) { abs_scores.push(Math.abs(d.link_score))
                                            , pvalues.push(d.link_pvalue);
                                        
                                            if (d.link_score >= 0) {
                                                p_scores.push(d.link_score);
                                            } else {
                                                n_scores.push(d.link_score);
                                            }
                });
                
                link = link.data(links);
                
                link.exit().remove();
                 
                var newLink = link.enter().append("path")
                                .attr("class", "link")                    
                                .attr('d', d => line(d.source.path(d.target)))
                                .style("stroke", function(d) { return d.link_color; })
                                .on("mouseover", mouseovered_link)
                                .on("mouseout", mouseouted);       
      
                link = link.merge(newLink);
                
                var linkLine = {"line": line, "link": link}
                
                function mouseovered_node(d) {
      
                    peak_data = $node_data.data
                    
                    if (Number.isNaN(Number(d.data[peak_data[0]]))) {                           
                        var init_value = d.data[peak_data[0]]                                   
                    } else if (typeof Number(d.data[peak_data[0]]) == 'number') { 
                        var init_value = Number(d.data[peak_data[0]]).toFixed(3)
                    }
                                
                    html_line = "\\""+ peak_data[0] + "\\",\\"" + init_value + "\\"";
                                    
                    peak_data.forEach(function(p) { 
                                    
                        if (p !== peak_data[0]) {
                            if (Number.isNaN(Number(d.data[p]))) {
                                var data_value = d.data[p];
                            } else if (typeof Number(d.data[p]) == 'number') {
                                var data_value = Number(d.data[p]).toFixed(3);
                            }
                  
                            html_line = html_line + "\\n\\"" + p + "\\",\\"" + data_value + "\\"";
                        }
                    });
                    
                    displayNodeData(html_line)
                    
                    node
                        .each(function(n) { n.target = n.source = false; });
                    
                    link
                        .classed("link--target", function(l) { if (l.target === d) return l.source.source = true; })
                        .classed("link--source", function(l) { if (l.source === d) return l.target.target = true; })
                        .filter(function(l) { return l.target === d || l.source === d; })
                        .each(function() { this.parentNode.appendChild(this); });
                     
                    node
                        .classed("node--both", function(n) { return n.source && n.target; })
                        .classed("node--target", function(n) { return n.target; })
                        .classed("node--source", function(n) { return n.source; });
                     
                    link.style('opacity', o => (o.source === d || o.target === d ? 1 : $linkFadeOpacity));
                }
                
                function mouseovered_link(d) {
                    
                    node
                        .each(function(n) { n.target = true; n.source = true; });
                    
                    link
                        .classed("link--source", function(l) { if (l.source.data.id === d.source.data.id) return l.target.target = true; });        
                    
                    node    
                        .classed("node--target", function(n) { if (n.data.id == d.target.data.id) return n.target; })
                        .classed("node--source", function(n) { if (n.data.id == d.source.data.id) return n.source; });
                        
                    link.style('opacity', o => (o.source === d.source || o.target === d.source ? 1 : $linkFadeOpacity))
                    
                    var source = d.source.data.Label;
                    var target = d.target.data.Label;    
                     
                    html_line = "\\"Source\\",\\""+ source + "\\"\\n\\"Target\\",\\"" + target + "\\"\\n\\"Pvalue\\"," + d.link_pvalue.toPrecision(3) + "\\n\\"Score\\"," + d.link_score.toPrecision(3)
                    
                    displayNodeData(html_line)
                    
                }
                
                function mouseouted(d) {
                    
                    d3.select('#nodedataPanel').selectAll("*").remove();
                    
                    link
                        .classed("link--target", false)
                        .classed("link--source", false);
        
                    node
                        .classed("node--both", false)
                        .classed("node--target", false)
                        .classed("node--source", false);
                     
                    link.style('opacity', 1);    
                    node.style('opacity', 1);
                }
                
                function packageHierarchy(classes) {
                    var map = {};
                    
                    function find(id, data) {
                        var node = map[id], i;
                        if (!node) {
                            node = map[id] = data || {id: id, children: []};
                            if (id.length) {
                                node.parent = find(id.substring(0, i = id.lastIndexOf("#")));
                                node.parent.children.push(node);
                                node.key = id.substring(i + 1);
                            }
                        }
                        return node;
                    }
                    
                    classes.forEach(function(d) {
                        find(d.id, d);
                    });
                    
                    return map[""];
                }
                
                function packageImports(nodes) {
                    var map = {}, imports = [];
    
                    nodes.forEach(function(d) {
                        map[d.data.id] = d;
                    });
                    
                    nodes.forEach(function(d) {
                        if (d.data.imports) Object.keys(d.data.imports).forEach(function(i) {    
                            imports.push({source: map[d.data.id], target: map[i]});
                        });
                    });
                    
                    return imports;
                }
                
                return linkLine;
            }
            
            function filterData(threshold, filtType) {
            
                const data = flareData.map(a => ({...a}));
                 
                var FlareData = []
                 
                //Remove nodes from imports with weight below threshold
                for (var i = 0; i < data.length; i++) {
                    var flare = data[i];
                    
                    var links = flare.imports;
                    var newLinks = {}
                     
                    for (const [key, value] of Object.entries(links)) {
                        
                        var link_score = value["link_score"];
                        var link_pvalue = value["link_pvalue"];
                        var link_color = value["link_color"];
                        
                        if (filtType == 'score_abs') {
                            
                            if (Math.abs(link_score) >= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }      
                        } else if (filtType == 'score_neg') {
                        
                            if (link_score <= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }
                            
                        } else if (filtType == 'score_pos') {
                            
                            if (link_score >= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }
                            
                        } else if (filtType == 'pvalue') {
                            if (link_pvalue <= threshold) {
                                newLinks[key] = {"link_score": link_score
                                                , "link_pvalue": link_pvalue
                                                , "link_color": link_color};
                            }
                        }
                    }
            
                    flare.imports = newLinks;
                    
                    FlareData.push(flare)
                }
                
                return FlareData;
            }
            
            function displayNodeData(datasetText) {
                
                d3.select('#nodedataPanel').selectAll("*").remove();
                
                var rows  = d3.csvParseRows(datasetText),
                table = d3.select('#nodedataPanel').append('table')
                                .style("border-collapse", "collapse")
                                .style("border", "2px black solid");
                
                var tablebody = table.append("tbody");
                            
                rows = tablebody
                        .selectAll("tr")
                        .data(rows)
                        .enter()
                        .append("tr");
     
                cells = rows.selectAll("td")            		
                        .data(function(d) { return d; })
                        .enter()
                        .append("td")
                        .text(function(d) { return d; })
                        .style("border", "1px black solid")
                        .style("font-size", "15px");
            };
        }

        redraw();

        // Redraw based on the new size whenever the browser window is resized.
        window.addEventListener("resize", redraw);       
        '''

        return js_text

    def __getHTML(self):

        html_text = '''

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <head>
	        <meta charset="utf-8">
	        <meta http-equiv="X-UA-Compatible" content="IE=edge">
	        <meta name="viewport" content="width=device-width, initial-scale=1.0">
	        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <link rel="stylesheet" type="text/css" href="https://rawgit.com/rzajac/angularjs-slider/master/dist/rzslider.css">
        </head>

        <style> $css_text </style>

        <body ng-app="rzSliderDemo">
		        <div class="row" ng-controller="MainCtrl">
			        <div class="col-4">
				        <div class="row col-2-auto">
					        <form id="filterType">
                                <input type='radio' id="scoreRadio" value="Corr. coeff" name="mode" ng-click="score_toggle()" checked/> Corr. coeff
                                <input type='radio' id="pvalueRadio" value="Pvalue" name="mode" ng-click="pvalue_toggle()"/> Pvalue
                            </form>
                        </div>
                
                        <div class="row col-3-auto">
                            <form id="scoreSelect">
                                <input type="radio" id="PosScoreRadio" name="mode" value="Positve" ng-click="pos_toggle()"/> Positive
                                <input type="radio" id="NegScoreRadio" name="mode" value="Negative" ng-click="neg_toggle()"/> Negative
                                <input type="radio" id="AbsScoreRadio" name="mode" value="Absolute" ng-click="abs_toggle()" checked/> Absolute
                            </form>
                        </div>
              
                        <div ng-show="abs_visible" class="row">
                            <rzslider id="abs_slider" class="abs_slider" rz-slider-model="abs_slider.value" rz-slider-options="abs_slider.options"></rzslider>
                        </div>
                        <div ng-show="pos_visible" class="row">
                            <rzslider id="pos_slider" class="pos_slider" rz-slider-model="pos_slider.value" rz-slider-options="pos_slider.options"></rzslider>
                        </div>
                        <div ng-show="neg_visible" class="row">
                            <rzslider id="neg_slider" class="neg_slider" rz-slider-model="neg_slider.value" rz-slider-options="neg_slider.options"></rzslider>
                        </div>
                        <div ng-show="pvalue_visible" class="row">
                            <rzslider id="pvalue_slider" class="pvalue_slider" rz-slider-model="pvalue_slider.value" rz-slider-options="pvalue_slider.options"></rzslider>
                        </div>
                                        
                        <div class="row">
                            <rzslider id="tension_slider" class="tension_slider" rz-slider-model="tension_slider.value" rz-slider-options="tension_slider.options"></rzslider>
                        </div>
                                        
                        <div id="save" class="row">
                            <button data-ng-click="savebutton()">Save</button>
                        </div>
					</div>		
			    </div>
			    
                <div id="edgeBundlePanel"></div>
        </body>
	    
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>	
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
	    
	    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"></script>
	    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular-animate.min.js"></script>
	    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular-aria.min.js"></script>
	    <script src="https://ajax.googleapis.com/ajax/libs/angular_material/1.0.0/angular-material.min.js"></script>        		
	    <script src="https://rawgit.com/rzajac/angularjs-slider/master/dist/rzslider.js"></script>
	    
        <script src="https://d3js.org/d3.v5.min.js"></script>
        
        <script>
            (function(){var g=typeof exports!="undefined"&&exports||this;var b='<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">';function e(h){return h&&h.lastIndexOf("http",0)==0&&h.lastIndexOf(window.location.host)==-1}function a(k,m){var h=k.querySelectorAll("image");var l=h.length;if(l==0){m()}for(var j=0;j<h.length;j++){(function(q){var o=q.getAttributeNS("http://www.w3.org/1999/xlink","href");if(o){if(e(o.value)){console.warn("Cannot render embedded images linking to external hosts: "+o.value);return}}var p=document.createElement("canvas");var i=p.getContext("2d");var n=new Image();o=o||q.getAttribute("href");n.src=o;n.onload=function(){p.width=n.width;p.height=n.height;i.drawImage(n,0,0);q.setAttributeNS("http://www.w3.org/1999/xlink","href",p.toDataURL("image/png"));l--;if(l==0){m()}};n.onerror=function(){console.log("Could not load "+o);l--;if(l==0){m()}}})(h[j])}}function f(h,k){var r="";var q=document.styleSheets;for(var o=0;o<q.length;o++){try{var u=q[o].cssRules}catch(s){console.warn("Stylesheet could not be loaded: "+q[o].href);continue}if(u!=null){for(var n=0;n<u.length;n++){var t=u[n];if(typeof(t.style)!="undefined"){var p=null;try{p=h.querySelector(t.selectorText)}catch(m){console.warn('Invalid CSS selector "'+t.selectorText+'"',m)}if(p){var l=k?k(t.selectorText):t.selectorText;r+=l+" { "+t.style.cssText+" }\\n"}else{if(t.cssText.match(/^@font-face/)){r+=t.cssText+"\\n"}}}}}}return r}function d(i,k,j){var h=(i.viewBox.baseVal&&i.viewBox.baseVal[j])||(k.getAttribute(j)!==null&&!k.getAttribute(j).match(/%$$/)&&parseInt(k.getAttribute(j)))||i.getBoundingClientRect()[j]||parseInt(k.style[j])||parseInt(window.getComputedStyle(i).getPropertyValue(j));return(typeof h==="undefined"||h===null||isNaN(parseFloat(h)))?0:h}function c(h){h=encodeURIComponent(h);h=h.replace(/%([0-9A-F]{2})/g,function(i,j){var k=String.fromCharCode("0x"+j);return k==="%"?"%25":k});return decodeURIComponent(h)}g.svgAsDataUri=function(j,i,h){i=i||{};i.scale=i.scale||1;var k="http://www.w3.org/2000/xmlns/";a(j,function(){var u=document.createElement("div");var r=j.cloneNode(true);var l,t;if(j.tagName=="svg"){l=i.width||d(j,r,"width");t=i.height||d(j,r,"height")}else{if(j.getBBox){var o=j.getBBox();l=o.x+o.width;t=o.y+o.height;r.setAttribute("transform",r.getAttribute("transform").replace(/translate\(.*?\)/,""));var p=document.createElementNS("http://www.w3.org/2000/svg","svg");p.appendChild(r);r=p}else{console.error("Attempted to render non-SVG element",j);return}}r.setAttribute("version","1.1");r.setAttributeNS(k,"xmlns","http://www.w3.org/2000/svg");r.setAttributeNS(k,"xmlns:xlink","http://www.w3.org/1999/xlink");r.setAttribute("width",l*i.scale);r.setAttribute("height",t*i.scale);r.setAttribute("viewBox",[i.left||0,i.top||0,l,t].join(" "));u.appendChild(r);var q=f(j,i.selectorRemap);var v=document.createElement("style");v.setAttribute("type","text/css");v.innerHTML="<![CDATA[\\n"+q+"\\n]]>";var n=document.createElement("defs");n.appendChild(v);r.insertBefore(n,r.firstChild);var p=b+u.innerHTML;var m="data:image/svg+xml;base64,"+window.btoa(c(p));if(h){h(m)}})};g.svgAsPngUri=function(j,i,h){g.svgAsDataUri(j,i,function(k){var l=new Image();l.onload=function(){var n=document.createElement("canvas");n.width=l.width;n.height=l.height;var o=n.getContext("2d");if(i&&i.backgroundColor){o.fillStyle=i.backgroundColor;o.fillRect(0,0,n.width,n.height)}o.drawImage(l,0,0);var m=document.createElement("a");h(n.toDataURL("image/png"))};l.src=k})};g.saveSvgAsPng=function(j,i,h){h=h||{};g.svgAsPngUri(j,h,function(l){var k=document.createElement("a");k.download=i;k.href=l;document.body.appendChild(k);k.addEventListener("click",function(m){k.parentNode.removeChild(k)});k.click()})}})();
        </script>

        <script> $js_text </script>
        '''

        return html_text

    def __getHTMLdashboard(self):

        html_text = '''
        
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <style> $css_text </style>
                
        <head>
	        <meta charset="utf-8">
	        <meta http-equiv="X-UA-Compatible" content="IE=edge">
	        <meta name="viewport" content="width=device-width, initial-scale=1.0">	
	        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">	
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <link rel="stylesheet" type="text/css" href="https://rawgit.com/rzajac/angularjs-slider/master/dist/rzslider.css">
        </head>

        <body ng-app="rzSliderDemo">
	        <div class="container-fluid py-5">
		        <div class="row" ng-controller="MainCtrl">
			        <div class="col-lg-9 col-12">
				        <div class="row">
					        <div class="col-md-12 mb-3">
						        <div class="card summary">
							        <div class="card-header">
								        <h4>Hierarchical Edge Bundle</h4>
							        </div>
							        <div class="card-body">
								        <div id="edgeBundlePanel"></div>
							        </div>
						        </div>
					        </div>					
				        </div>		
			        </div>
			        <div class="col-lg-3 col-12">
				        <div class="card mb-3">
					        <div class="card-body">						
						        <div class="input-group mb-3">
							        <div class="card-body">
                    
                                        <div class="row col-2-auto">
                                            <form id="filterType">
                                                <input type='radio' id="scoreRadio" value="Corr. coeff" name="mode" ng-click="score_toggle()" checked/> Corr. coeff
                                                <input type='radio' id="pvalueRadio" value="Pvalue" name="mode" ng-click="pvalue_toggle()"/> Pvalue
                                            </form>
                                        </div>
                
                                        <div class="row col-3-auto">
                                            <form id="scoreSelect">
                                                <input type="radio" id="PosScoreRadio" name="mode" value="Positve" ng-click="pos_toggle()"/> Positive
                                                <input type="radio" id="NegScoreRadio" name="mode" value="Negative" ng-click="neg_toggle()"/> Negative
                                                <input type="radio" id="AbsScoreRadio" name="mode" value="Absolute" ng-click="abs_toggle()" checked/> Absolute
                                            </form>
                                        </div>
              
                                        <div ng-show="abs_visible" class="row">
                                            <rzslider id="abs_slider" class="abs_slider" rz-slider-model="abs_slider.value" rz-slider-options="abs_slider.options"></rzslider>
                                        </div>
                                        <div ng-show="pos_visible" class="row">
                                            <rzslider id="pos_slider" class="pos_slider" rz-slider-model="pos_slider.value" rz-slider-options="pos_slider.options"></rzslider>
                                        </div>
                                        <div ng-show="neg_visible" class="row">
                                            <rzslider id="neg_slider" class="neg_slider" rz-slider-model="neg_slider.value" rz-slider-options="neg_slider.options"></rzslider>
                                        </div>
                                        <div ng-show="pvalue_visible" class="row">
                                            <rzslider id="pvalue_slider" class="pvalue_slider" rz-slider-model="pvalue_slider.value" rz-slider-options="pvalue_slider.options"></rzslider>
                                        </div>
                                        
                                        <div class="row">
                                            <rzslider id="tension_slider" class="tension_slider" rz-slider-model="tension_slider.value" rz-slider-options="tension_slider.options"></rzslider>
                                        </div>
                                        
                                        <div id="save" class="row">
                                            <button data-ng-click="savebutton()">Save</button>
                                        </div>
                                    </div>
				                </div>
					        </div>
				        </div>
				        <div class="card">
					        <div class="card-header">
						        <h4>Node Data</h4>
					        </div>
					        <div class="card-body">
						        <div id="nodedataPanel"></div>
						    </div>
					    </div>
				    </div>
			    </div>
			</div>
	    </body>

	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>	
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
	    
	    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"></script>
	    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular-animate.min.js"></script>
	    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular-aria.min.js"></script>
	    <script src="https://ajax.googleapis.com/ajax/libs/angular_material/1.0.0/angular-material.min.js"></script>        		
	    <script src="https://rawgit.com/rzajac/angularjs-slider/master/dist/rzslider.js"></script>

        <script src="https://d3js.org/d3.v5.min.js"></script>
        
        <script>
            (function(){var g=typeof exports!="undefined"&&exports||this;var b='<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">';function e(h){return h&&h.lastIndexOf("http",0)==0&&h.lastIndexOf(window.location.host)==-1}function a(k,m){var h=k.querySelectorAll("image");var l=h.length;if(l==0){m()}for(var j=0;j<h.length;j++){(function(q){var o=q.getAttributeNS("http://www.w3.org/1999/xlink","href");if(o){if(e(o.value)){console.warn("Cannot render embedded images linking to external hosts: "+o.value);return}}var p=document.createElement("canvas");var i=p.getContext("2d");var n=new Image();o=o||q.getAttribute("href");n.src=o;n.onload=function(){p.width=n.width;p.height=n.height;i.drawImage(n,0,0);q.setAttributeNS("http://www.w3.org/1999/xlink","href",p.toDataURL("image/png"));l--;if(l==0){m()}};n.onerror=function(){console.log("Could not load "+o);l--;if(l==0){m()}}})(h[j])}}function f(h,k){var r="";var q=document.styleSheets;for(var o=0;o<q.length;o++){try{var u=q[o].cssRules}catch(s){console.warn("Stylesheet could not be loaded: "+q[o].href);continue}if(u!=null){for(var n=0;n<u.length;n++){var t=u[n];if(typeof(t.style)!="undefined"){var p=null;try{p=h.querySelector(t.selectorText)}catch(m){console.warn('Invalid CSS selector "'+t.selectorText+'"',m)}if(p){var l=k?k(t.selectorText):t.selectorText;r+=l+" { "+t.style.cssText+" }\\n"}else{if(t.cssText.match(/^@font-face/)){r+=t.cssText+"\\n"}}}}}}return r}function d(i,k,j){var h=(i.viewBox.baseVal&&i.viewBox.baseVal[j])||(k.getAttribute(j)!==null&&!k.getAttribute(j).match(/%$$/)&&parseInt(k.getAttribute(j)))||i.getBoundingClientRect()[j]||parseInt(k.style[j])||parseInt(window.getComputedStyle(i).getPropertyValue(j));return(typeof h==="undefined"||h===null||isNaN(parseFloat(h)))?0:h}function c(h){h=encodeURIComponent(h);h=h.replace(/%([0-9A-F]{2})/g,function(i,j){var k=String.fromCharCode("0x"+j);return k==="%"?"%25":k});return decodeURIComponent(h)}g.svgAsDataUri=function(j,i,h){i=i||{};i.scale=i.scale||1;var k="http://www.w3.org/2000/xmlns/";a(j,function(){var u=document.createElement("div");var r=j.cloneNode(true);var l,t;if(j.tagName=="svg"){l=i.width||d(j,r,"width");t=i.height||d(j,r,"height")}else{if(j.getBBox){var o=j.getBBox();l=o.x+o.width;t=o.y+o.height;r.setAttribute("transform",r.getAttribute("transform").replace(/translate\(.*?\)/,""));var p=document.createElementNS("http://www.w3.org/2000/svg","svg");p.appendChild(r);r=p}else{console.error("Attempted to render non-SVG element",j);return}}r.setAttribute("version","1.1");r.setAttributeNS(k,"xmlns","http://www.w3.org/2000/svg");r.setAttributeNS(k,"xmlns:xlink","http://www.w3.org/1999/xlink");r.setAttribute("width",l*i.scale);r.setAttribute("height",t*i.scale);r.setAttribute("viewBox",[i.left||0,i.top||0,l,t].join(" "));u.appendChild(r);var q=f(j,i.selectorRemap);var v=document.createElement("style");v.setAttribute("type","text/css");v.innerHTML="<![CDATA[\\n"+q+"\\n]]>";var n=document.createElement("defs");n.appendChild(v);r.insertBefore(n,r.firstChild);var p=b+u.innerHTML;var m="data:image/svg+xml;base64,"+window.btoa(c(p));if(h){h(m)}})};g.svgAsPngUri=function(j,i,h){g.svgAsDataUri(j,i,function(k){var l=new Image();l.onload=function(){var n=document.createElement("canvas");n.width=l.width;n.height=l.height;var o=n.getContext("2d");if(i&&i.backgroundColor){o.fillStyle=i.backgroundColor;o.fillRect(0,0,n.width,n.height)}o.drawImage(l,0,0);var m=document.createElement("a");h(n.toDataURL("image/png"))};l.src=k})};g.saveSvgAsPng=function(j,i,h){h=h||{};g.svgAsPngUri(j,h,function(l){var k=document.createElement("a");k.download=i;k.href=l;document.body.appendChild(k);k.addEventListener("click",function(m){k.parentNode.removeChild(k)});k.click()})}})();
        </script>

        <script> $js_text </script>               
        '''

        return html_text