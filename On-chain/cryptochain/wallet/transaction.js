const uuid = require('uuid/v1');
const delay = require('delay');
const { verifySignature } = require('../util');
const { REWARD_INPUT, MINING_REWARD } = require('../config');

class Transaction {
    constructor({ senderWallet, recipient, message, amount, outputMap, input }) {
        this.id = uuid();
        this.outputMap = outputMap || this.createOutputMap({ senderWallet, message, recipient });
        this.input = input || this.createInput({ senderWallet, outputMap: this.outputMap });
    }
    
    createOutputMap({ senderWallet, message, recipient, amount }) {
        const outputMap = {};
        outputMap[recipient] = message;
        if ( outputMap[recipient] === 'leave'){
          // function myFunc(arg) {
          //   return Number(arg);
          // }
          // outputMap[senderWallet.publicKey] = myFunc;
          // setTimeout(myFunc, 15000, '0');
          outputMap[senderWallet.publicKey] = 0;
        } else {
          outputMap[senderWallet.publicKey] = senderWallet.balance - 1;
        }
        return outputMap;
    }

    createInput({ senderWallet, outputMap }) {
        return{
            timestamp: Date.now(),
            address: senderWallet.publicKey,
            signature: senderWallet.sign(outputMap)
        };
    }

    static validTransaction(transaction) {
        const { input: { address, signature }, outputMap } = transaction;
    
        if (!verifySignature({ publicKey: address, data: outputMap, signature })) {
          console.error(`Invalid signature from ${address}`);
          return false;
        }
    
        return true;
    }

    static rewardTransaction({ minerWallet }) {
      return new this({
        input: REWARD_INPUT,
        outputMap: { [minerWallet.publicKey]: MINING_REWARD }  
      });
    }
}

module.exports = Transaction; 