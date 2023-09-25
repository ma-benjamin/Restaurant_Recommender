const database = document.querySelector('.table');
const entry = document.createElement('div');

database.appendChild(entry)
entry.textContent = "1"

data = open("./zipcodes/07039.json", 'r');
entry.textContent = data.read();

console.log("1")
