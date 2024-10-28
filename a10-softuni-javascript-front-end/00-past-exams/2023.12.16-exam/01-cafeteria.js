function cafeteriaManagement(input) {
  const n = Number(input.shift());
  const baristas = {};

  for (let i = 0; i < n; i++) {
    const [name, shift, coffeeList] = input.shift().split(" ");
    baristas[name] = {
      shift: shift,
      drinks: coffeeList.split(","),
    };
  }

  for (let commandLine of input) {
    if (commandLine === "Closed") {
      break;
    }

    const [command, ...args] = commandLine.split(" / ");
    const baristaName = args[0];

    switch (command) {
      case "Prepare": {
        const [shift, coffeeType] = args.slice(1);
        if (
          baristas[baristaName].shift === shift &&
          baristas[baristaName].drinks.includes(coffeeType)
        ) {
          console.log(`${baristaName} has prepared a ${coffeeType} for you!`);
        } else {
          console.log(
            `${baristaName} is not available to prepare a ${coffeeType}.`
          );
        }
        break;
      }

      case "Change Shift": {
        const newShift = args[1];
        baristas[baristaName].shift = newShift;
        console.log(`${baristaName} has updated his shift to: ${newShift}`);
        break;
      }

      case "Learn": {
        const newCoffeeType = args[1];
        if (baristas[baristaName].drinks.includes(newCoffeeType)) {
          console.log(`${baristaName} knows how to make ${newCoffeeType}.`);
        } else {
          baristas[baristaName].drinks.push(newCoffeeType);
          console.log(
            `${baristaName} has learned a new coffee type: ${newCoffeeType}.`
          );
        }
        break;
      }

      default:
        break;
    }
  }

  for (const [name, details] of Object.entries(baristas)) {
    console.log(
      `Barista: ${name}, Shift: ${details.shift}, Drinks: ${details.drinks.join(
        ", "
      )}`
    );
  }
}

// Test Case #1:
cafeteriaManagement([
  "3",
  "Alice day Espresso,Cappuccino",
  "Bob night Latte,Mocha",
  "Carol day Americano,Mocha",
  "Prepare / Alice / day / Espresso",
  "Change Shift / Bob / night",
  "Learn / Carol / Latte",
  "Learn / Bob / Latte",
  "Prepare / Bob / night / Latte",
  "Closed",
]);

// Expected output:
// Alice has prepared a Espresso for you!
// Bob has updated his shift to: night
// Carol has learned a new coffee type: Latte.
// Bob knows how to make Latte.
// Bob has prepared a Latte for you!
// Barista: Alice, Shift: day, Drinks: Espresso, Cappuccino
// Barista: Bob, Shift: night, Drinks: Latte, Mocha
// Barista: Carol, Shift: day, Drinks: Americano, Mocha, Latte

// Test Case #2:
cafeteriaManagement([
  "4",
  "Alice day Espresso,Cappuccino",
  "Bob night Latte,Mocha",
  "Carol day Americano,Mocha",
  "David night Espresso",
  "Prepare / Alice / day / Espresso",
  "Change Shift / Bob / day",
  "Learn / Carol / Latte",
  "Prepare / Bob / night / Latte",
  "Learn / David / Cappuccino",
  "Prepare / Carol / day / Cappuccino",
  "Change Shift / Alice / night",
  "Learn / Bob / Mocha",
  "Prepare / David / night / Espresso",
  "Closed",
]);

// Expected output:
// Alice has prepared a Espresso for you!
// Bob has updated his shift to: day
// Carol has learned a new coffee type: Latte.
// Bob is not available to prepare a Latte.
// David has learned a new coffee type: Cappuccino.
// Carol is not available to prepare a Cappuccino.
// Alice has updated his shift to: night
// Bob knows how to make Mocha.
// David has prepared a Espresso for you!
// Barista: Alice, Shift: night, Drinks: Espresso, Cappuccino
// Barista: Bob, Shift: day, Drinks: Latte, Mocha
// Barista: Carol, Shift: day, Drinks: Americano, Mocha, Latte
// Barista: David, Shift: night, Drinks: Espresso, Cappuccino
