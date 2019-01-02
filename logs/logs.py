#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logging.basicConfig( 
    level = logging.DEBUG,   #мин. уровень вывода
    #filename = 'test.log' #показ. путь к файлу с логами
    format = '%(levelname)-8s [%(asctime)s] %(message)s'
) 


logging.debug( 'debugging' )
logging.info( 'information' )
logging.warning( 'warn' )
logging.error( 'bad' )
logging.critical ( 'very bad' )

