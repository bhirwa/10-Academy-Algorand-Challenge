from typing import Optional
from fastapi import FastAPI

from algosdk import account, encoding , mnemonic 
from algosdk.future.transaction import PaymentTxn
from algosdk.future.transaction import AssetConfigTxn
from algosdk.error import WrongChecksumError ,WrongMnemonicLengthError
from algosdk.v2client import algod , indexer

from schemes import * 

algod_client=algod.AlgodClient("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","http://localhost:4001") #Initializing the algod client
indexer_client=indexer.IndexerClient("","http://localhost:8980") #initializing the validator

app = FastAPI() #Create a base application instance
