# RunArbIfDown.py | This file is used as an extra layer to catch exceptions and keep the software running

import time
import settings
import ArbitrageMain

#Time in seconds
DOWNTIME = settings.RUNTIME+1
Path = settings.PATH

def start():
    for i in range(0, 1000000):
        filename = 'check.txt'
        f = open(Path / filename, "r")
        line = f.readline()
        print(line)
        f.close()

        if (time.time() - float(line)) > DOWNTIME:
            print('REBOOTING THE ARBITRAGE')
            try:
                ArbitrageMain.main()
            except Exception as e:
                print(f'ARBITRAGE hit an error: {e}')
                pass

        else:
            print('ARBITRAGE IS STILL RUNNING')
            print('waiting the following seconds:')
            print(DOWNTIME)
        print('program was checked if running at' + time.strftime('%X %x %Z'))
        time.sleep(DOWNTIME)
