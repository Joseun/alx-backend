// Stocks with job queues

const util = require('util');
const express = require('express');

const redis = require('redis');

const listProducts = [
  {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];

function getItemById(id) {
  const product = listProducts.filter((product) => product.Id == id);
  return product[0];
}

const app = express();
app.listen(1245);

app.get('/list_products', (req, res) => {
  res.send(
    listProducts.map((product) => {
      product.initialAvailableQuantity = product.stock;
      delete product.stock;
      product.itemName = product.name;
      delete product.name;
      product.ItemId = product.Id;
      delete product.Id;
      return product;
    })
  );
});

app.get('/list_products/:itemId', (req, res) => {
  const id = req.params.itemId;
  getCurrentReservedStockById(id)
    .then((item) => {
      res.send(item)
    });
})

app.get('/reserve_product/:itemId', (req, res) => {
  const id = req.params.itemId;
  const product = getItemById(id);
  if (!product) {
    res.send({"status":"Product not found"});
  } else if (product.stock < 1) {
    res.send({"status":"Not enough stock available","itemId":id});
  } else {
    reserveStockById(id, 1)
    res.send({"status":"Reservation confirmed","itemId":id})
  }
})

const client = redis.createClient();

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock)
}

async function getCurrentReservedStockById(itemId) {
  const getStock = util.promisify(client.get).bind(client);
  //reserveStockById(itemId, 30)
  const currentStock = await getStock(`item.${itemId}`)
  const product = getItemById(itemId);
  if (product) {
    product.initialAvailableQuantity = product.stock;
    delete product.stock;
    product.itemName = product.name;
    delete product.name;
    product.ItemId = product.Id;
    delete product.Id;
    product.currentQuantity = currentStock;
    return product;
  }
  return {"status":"Product not found"};
}
