from src.websites import WEBSITES
from src.managers.managerfactory import ManagerFactory
from src.websites.websitefactory import WebsiteFactory
from src.log import logger
import traceback

def test():
    counter = 0
    succes = 0
    fails = {}
    logger.debug('Test in progress...')
    logger.debug('0/' + str(len(WEBSITES)) + '\tSucces: 0\tFails: 0')
    
    manager_factory = ManagerFactory()
    manager = manager_factory.get_manager()
    website_factory = WebsiteFactory()
    
    for website in WEBSITES.values():
        try :
            website = website_factory.get_website(website.TEST_KEY)
            manager.set(website, test=True)
            succes+=1
        except Exception as e:
            fails[website.KEY] = str(traceback.format_exc())
        
        counter+=1
        logger.debug(str(counter) + '/' + str(len(WEBSITES)) + '\tSucces: ' + str(succes) + '\tFails: ' + str(len(fails)), CR=True, flush=True)

    if(len(fails) == 0):
        logger.debug('OK')
    else:
        for fail in fails.keys():
            logger.debug('=============')
            logger.debug(fail + " : " + fails[fail])

if __name__ == "__main__":
	try:
		test()
	except KeyboardInterrupt:
		None