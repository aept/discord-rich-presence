import os
import rpc
import time
import json
from time import mktime
from logger import logger

def main():

    isConfig = os.path.isfile('config.json')

    if isConfig:
        file = open('config.json', encoding='utf8')
        config = json.load(file)

        applicationId = config['applicationId']
        timestamp = config['timestamps']

        if applicationId and not applicationId.isspace():
            application_id = applicationId
            rpc_client = rpc.DiscordIpcClient.for_platform(application_id)
            print('RPC connection established.')

            print('Initializing presence in 5 seconds...')
            time.sleep(5)
            
            while True:
                activity = config['presences'][config['presenceId']]
                
                if timestamp == True:
                    start_time = mktime(time.localtime())

                    newActivity = {
                        **activity,
                        "timestamps": {
                            "start": start_time
                        }
                    }
                    activity.update(newActivity);

                rpc_client.set_activity(activity)
                print('Presence initialized succesfully!')
                time.sleep(900)
        else:
            logger.error('ClientID is required.')
    else:
        logger.error('Config file does not exists!')

if __name__ == '__main__':
    main()
