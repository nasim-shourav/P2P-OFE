DEPENDENCIES TO INSTALL: 

npm init -y
npm i jest@23.6.0 --save-dev 
npm i hex-to-binary@1.0.1 --save
npm i express@4.16.3 --save  
npm i nodemon@1.18.4 --save-dev 
npm i body-parser@1.18.3 --save
npm i redis@2.8.0 --save
redis-server --daemonize yes
npm i cross-env@5.2.0 --save-dev
npm i request@2.88.0 --save 
npm i elliptic@6.4.1 --save
npm i uuid@3.3.2 --save

####################################################################
####################################################################

COMMAND FOR RUNNING A NODE:

npm run dev (will start a node at port 3000) or;  
npm run dev-peer (will start a node at any port from 3001 to 4000). 

####################################################################
####################################################################

The API's are:

1. localhost:PORTNUMBER/api/blocks ==> to get the blocks in the chain
2. localhost:PORTNUMBER/api/transact ==> to post a transaction

Sample example of how to post a transaction (in json format): 

{
	"recipient": "0495ee965eab6c0210696e093eb29be8cb263897aba12b76bdf168419d29b286d98e0a9acd2b8153c238b758ad29ff5f42650eda3370d0efd382ab2d5d6ccbc2a3",
	"message": "This is a test message"
}

3. localhost:PORTNUMBER/api/transaction-pool-map ==> to get the unmined transactions list.
4. localhost:PORTNUMBER/api/mine-transactions ==> will mine a block and then re-direct to localhost:PORTNUMBER/api/blocks.
4. localhost:PORTNUMBER/api/wallet-info ==> to get the info of how much reputation score that node has.