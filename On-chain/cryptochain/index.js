const bodyParser = require('body-parser');
const express = require('express');
const request = require('request');
const path = require('path');
const Blockchain = require('./blockchain');
const PubSub = require('./app/pubsub');
const TransactionPool = require('./wallet/transaction-pool');
const Wallet = require('./wallet');
const TransactionMiner = require('./app/transaction-miner');
const { MIN_BALANCE } = require('./config') //Minimum balance to maintain, taking data from main index.js
var _ = require('underscore');

const app = express();
const blockchain = new Blockchain();
const transactionPool = new TransactionPool();
const wallet = new Wallet();
const pubsub = new PubSub ({ blockchain, transactionPool });
const transactionMiner = new TransactionMiner({ blockchain, transactionPool, wallet, pubsub });

const DEFAULT_PORT =3000;
const ROOT_NODE_ADDRESS = `http://localhost:${DEFAULT_PORT}`;




app.use(bodyParser.json()); // A middleware to help the express to able to receive json formatted data 
app.use(express.static(path.join(__dirname, 'client/dist')));


app.get('/api/blocks', (req, res) => {
    const balance = Wallet.calculateBalance({ chain: blockchain.chain, address: wallet.publicKey });
    if ( balance > MIN_BALANCE){
        res.json(blockchain.chain);
    } else res.status(400).json({type: 'error', message: 'Insufficient Points' });
});

app.post('/api/mine', (req, res) => {
    const { data } = req.body;
    const balance = Wallet.calculateBalance({ chain: blockchain.chain, address: wallet.publicKey });
    if ( balance > MIN_BALANCE){
        blockchain.addBlock({ data });

        pubsub.broadcastChain();
    
        res.redirect('/api/blocks');
    } else res.status(400).json({type: 'error', message: 'Insufficient Points' });
   
});

app.post('/api/transact', (req, res) => {
    const { recipient, message } = req.body;
    const balance = Wallet.calculateBalance({ chain: blockchain.chain, address: wallet.publicKey });
    if ( balance > MIN_BALANCE){
        let transaction = transactionPool
            .existingTransaction({ inputAddress: wallet.publicKey });

        try {
            if (transaction) {
                transaction.update({ senderWallet: wallet, recipient, message }); 
            } else {
                transaction = wallet.createTransaction({
                    recipient,
                    message,
                    chain: blockchain.chain
                }); 
            }
        } catch(error) {
            return res.status(400).json({type: 'error', message: error.message });
        }

        transactionPool.setTransaction(transaction);

        pubsub.broadcastTransaction(transaction);

        res.json({ type: 'success', transaction });
    } else res.status(400).json({type: 'error', message: 'Insufficient Points' });
    
});

app.get('/api/transaction-pool-map', (req, res) => {
    const balance = Wallet.calculateBalance({ chain: blockchain.chain, address: wallet.publicKey });
    if ( balance > MIN_BALANCE){
        res.json(transactionPool.transactionMap);
    } else res.status(400).json({type: 'error', message: 'Insufficient Points' });
    
});

app.get('/api/mine-transactions', (req, res) => {
    const balance = Wallet.calculateBalance({ chain: blockchain.chain, address: wallet.publicKey });
    if ( balance > MIN_BALANCE){
        transactionMiner.mineTransactions();

        res.redirect('/api/blocks');
    } else res.status(400).json({type: 'error', message: 'Insufficient Points' });
    
});

app.get('/api/wallet-info', (req, res) => {
    const address = wallet.publicKey;
    const balance = Wallet.calculateBalance({ chain: blockchain.chain, address: wallet.publicKey });
    if ( balance > MIN_BALANCE){
        res.json({
            address,
            balance: Wallet.calculateBalance({ chain: blockchain.chain, address })
        }); 
    } else res.status(400).json({type: 'error', message: 'Insufficient Points' });
    
    
});

app.get('/api/known-addresses', (req, res) => {
    const addressMap = {};
    let arrayTwo = {};
    let fin = {};
    let aa = {};
    let KnV ={}
    for (let block of blockchain.chain) {
        for (transaction of block.data) {
            k = Object.keys(transaction.outputMap);
            KnV = Object.entries(transaction.outputMap);
            vals = Object.values(transaction.outputMap);    
            
            // key and value interchange
            let countries = Object.keys(transaction.outputMap).reduce((acc, k) => {
                let country = transaction.outputMap[k];
                acc[country] = acc[country] || [];
                acc[country].push(k);
                return acc;
              }, {});   
            

            // Finding valeus with specific keys  
            aa = countries["leave"];
            
            // Differentiating new array from the old one
            fin = _.difference(k, aa);
            
            console.log("====>", aa);
            console.log("Fin", fin);
           
            fin.forEach(recipient => addressMap[recipient] = recipient);
        }
        
    }
    res.json(Object.keys(addressMap));    
  });
    
    //__________This is to connect with the front-end
    
    app.get('*', (req, res) => {
        res.sendFile(path.join(__dirname,'client/dist/index.html'));
    });

    //__________This is to connect with the front-end

    const syncWithRootState = () => {
        request({ url: `${ROOT_NODE_ADDRESS}/api/blocks` }, (error, response, body) => {
            if (!error && response.statusCode === 200) {
                const rootChain = JSON.parse(body);
    
                console.log('replace chain on a sync with', rootChain);
                blockchain.replaceChain(rootChain);
            }
        });
    
        request({ url: `${ROOT_NODE_ADDRESS}/api/transaction-pool-map` }, (error, response, body) => {
            if(!error && response.statusCode === 200) {
                const rootTransactionPoolMap = JSON.parse(body);
    
                console.log('replace transaction pool map on a sync with', rootTransactionPoolMap);
                transactionPool.setMap(rootTransactionPoolMap);            
            }
        });
    }


// Creatig the peer port to connect the channel 

let PEER_PORT;

if (process.env.GENERATE_PEER_PORT == 'true') {
    PEER_PORT = DEFAULT_PORT + Math.ceil(Math.random() * 1000);
    // const nodes = [];    
    // console.log(nodes.forEach(nodes => nodes[PEER_PORT] = PEER_PORT));
}

const PORT = PEER_PORT || DEFAULT_PORT;
app.listen(PORT, () => {
    console.log(`listening at localhost:${PORT} and the id:${wallet.publicKey}`);
    

    // nodes.push(PORT);
    // console.log(nodes);
    if (PORT !== DEFAULT_PORT) {
        syncWithRootState();
    };
});

//console.log(p);


// "start-redis": "redis-server --daemonize yes" // npm run start-redis &&