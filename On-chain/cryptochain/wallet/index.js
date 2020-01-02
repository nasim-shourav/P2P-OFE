const Transaction = require('./transaction');
const { STARTING_BALANCE } = require('../config');
const { ec, cryptoHash } = require('../util');
const Blockchain = require('../index');

//const blockchain = new Blockchain();

class Wallet {
  constructor() {
    this.balance = STARTING_BALANCE;

    this.keyPair = ec.genKeyPair();

    this.publicKey = this.keyPair.getPublic().encode('hex');
  }

  sign(data) {
    return this.keyPair.sign(cryptoHash(data))
  }

  createTransaction({ recipient, message, chain }) { 
    if (chain) {
      this.balance = Wallet.calculateBalance({
        chain,
        address: this.publicKey
      });
    }

    
    return new Transaction({ senderWallet: this, recipient, message }); // amount
  }

  static calculateBalance({ chain, address }) {
    let hasConductedTransaction = false;
    let outputsTotal = 0;

    for (let i=chain.length-1; i>0; i--) {
      const block = chain[i];

      for (let transaction of block.data) {
        if (transaction.input.address === address) {
          hasConductedTransaction = true;
        }

        const addressOutput = transaction.outputMap[address];

        if (addressOutput) {
          outputsTotal = outputsTotal + addressOutput;
        }
      }

      if (hasConductedTransaction) {
        break;
      }
    }

    return hasConductedTransaction ? outputsTotal : STARTING_BALANCE + outputsTotal;
  }

  // static bal(){
  //   const trueBalance = Wallet.calculateBalance({
  //     chain,
  //     address: this.publicKey
  //   });

  //   return trueBalance;
  // }
};

module.exports = Wallet;