function scienceExperimentation(input) {
  const n = Number(input.shift());
  const chemicals = {};

  for (let i = 0; i < n; i++) {
    const [name, quantity] = input.shift().split(" # ");
    chemicals[name] = {
      quantity: Number(quantity),
      formula: null,
    };
  }

  for (let commandLine of input) {
    if (commandLine === "End") {
      break;
    }

    const [command, ...args] = commandLine.split(" # ");

    switch (command) {
      case "Mix": {
        const [chemical1, chemical2, amount] = args;
        const mixAmount = Number(amount);

        if (
          chemicals[chemical1] &&
          chemicals[chemical2] &&
          chemicals[chemical1].quantity >= mixAmount &&
          chemicals[chemical2].quantity >= mixAmount
        ) {
          chemicals[chemical1].quantity -= mixAmount;
          chemicals[chemical2].quantity -= mixAmount;
          console.log(
            `${chemical1} and ${chemical2} have been mixed. ${mixAmount} units of each were used.`
          );
        } else {
          console.log(
            `Insufficient quantity of ${chemical1}/${chemical2} to mix.`
          );
        }
        break;
      }

      case "Replenish": {
        const [chemical, amount] = args;
        const replenishAmount = Number(amount);

        if (!chemicals[chemical]) {
          console.log(`The Chemical ${chemical} is not available in the lab.`);
        } else {
          const currentQuantity = chemicals[chemical].quantity;
          const newQuantity = Math.min(currentQuantity + replenishAmount, 500);
          const addedAmount = newQuantity - currentQuantity;
          chemicals[chemical].quantity = newQuantity;
          if (newQuantity === 500) {
            console.log(
              `${chemical} quantity increased by ${addedAmount} units, reaching maximum capacity of 500 units!`
            );
          } else {
            console.log(
              `${chemical} quantity increased by ${addedAmount} units!`
            );
          }
        }
        break;
      }

      case "Add Formula": {
        const [chemical, formula] = args;

        if (!chemicals[chemical]) {
          console.log(`The Chemical ${chemical} is not available in the lab.`);
        } else {
          chemicals[chemical].formula = formula;
          console.log(`${chemical} has been assigned the formula ${formula}.`);
        }
        break;
      }

      default:
        break;
    }
  }

  for (const [name, details] of Object.entries(chemicals)) {
    if (details.formula) {
      console.log(
        `Chemical: ${name}, Quantity: ${details.quantity}, Formula: ${details.formula}`
      );
    } else {
      console.log(`Chemical: ${name}, Quantity: ${details.quantity}`);
    }
  }
}

// Test Case #1:
scienceExperimentation([
  "4",
  "Water # 200",
  "Salt # 100",
  "Acid # 50",
  "Base # 80",
  "Mix # Water # Salt # 50",
  "Replenish # Salt # 150",
  "Add Formula # Acid # H2SO4",
  "End",
]);

// Expected output:
// Water and Salt have been mixed. 50 units of each were used.
// Salt quantity increased by 150 units!
// Acid has been assigned the formula H2SO4.
// Chemical: Water, Quantity: 150
// Chemical: Salt, Quantity: 200
// Chemical: Acid, Quantity: 50, Formula: H2SO4
// Chemical: Base, Quantity: 80

// Test Case #2:
scienceExperimentation([
  "3",
  "Sodium # 300",
  "Chlorine # 100",
  "Hydrogen # 200",
  "Mix # Sodium # Chlorine # 200",
  "Replenish # Sodium # 250",
  "Add Formula # Sulfuric Acid # H2SO4",
  "Add Formula # Sodium # Na",
  "Mix # Hydrogen # Chlorine # 50",
  "End",
]);

// Expected output:
// Insufficient quantity of Sodium/Chlorine to mix.
// Sodium quantity increased by 200 units, reaching maximum capacity of 500 units!
// The Chemical Sulfuric Acid is not available in the lab.
// Sodium has been assigned the formula Na.
// Hydrogen and Chlorine have been mixed. 50 units of each were used.
// Chemical: Sodium, Quantity: 500, Formula: Na
// Chemical: Chlorine, Quantity: 50
// Chemical: Hydrogen, Quantity: 150
