function motoGPRace(input) {
  const n = Number(input.shift());
  const riders = {};

  for (let i = 0; i < n; i++) {
    const [name, fuel, position] = input.shift().split("|");
    riders[name] = {
      fuel: Number(fuel.trim().replace("%", "")),
      position: Number(position.trim()),
    };
  }

  for (let commandLine of input) {
    if (commandLine === "Finish") {
      break;
    }

    const [command, ...args] = commandLine.split(" - ");
    const riderName = args[0].trim();

    switch (command) {
      case "StopForFuel": {
        const minFuel = Number(args[1]);
        const changedPosition = Number(args[2]);
        if (riders[riderName].fuel < minFuel) {
          riders[riderName].position = changedPosition;
          console.log(
            `${riderName} stopped to refuel but lost his position, now he is ${changedPosition}.`
          );
        } else {
          console.log(`${riderName} does not need to stop for fuel!`);
        }
        break;
      }

      case "Overtaking": {
        const rider2Name = args[1].trim();
        if (riders[riderName].position < riders[rider2Name].position) {
          const tempPosition = riders[riderName].position;
          riders[riderName].position = riders[rider2Name].position;
          riders[rider2Name].position = tempPosition;
          console.log(`${riderName} overtook ${rider2Name}!`);
        }
        break;
      }

      case "EngineFail": {
        const lapsLeft = Number(args[1]);
        console.log(
          `${riderName} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`
        );
        delete riders[riderName];
        break;
      }

      default:
        break;
    }
  }

  for (const [name, details] of Object.entries(riders)) {
    console.log(`${name}\n  Final position: ${details.position}`);
  }
}

// Test Case #1:
motoGPRace([
  "3",
  "Valentino Rossi|100|1",
  "Marc Marquez|90|2",
  "Jorge Lorenzo|80|3",
  "StopForFuel - Valentino Rossi - 50 - 1",
  "Overtaking - Marc Marquez - Jorge Lorenzo",
  "EngineFail - Marc Marquez - 10",
  "Finish",
]);

// Expected output:
// Valentino Rossi does not need to stop for fuel!
// Marc Marquez overtook Jorge Lorenzo!
// Marc Marquez is out of the race because of a technical issue, 10 laps before the finish.
// Valentino Rossi
//   Final position: 1
// Jorge Lorenzo
//   Final position: 2

// Test Case #2:
motoGPRace([
  "4",
  "Valentino Rossi|100|1",
  "Marc Marquez|90|3",
  "Jorge Lorenzo|80|4",
  "Johann Zarco|80|2",
  "StopForFuel - Johann Zarco - 90 - 5",
  "Overtaking - Marc Marquez - Jorge Lorenzo",
  "EngineFail - Marc Marquez - 10",
  "Finish",
]);

// Expected output:
// Johann Zarco stopped to refuel but lost his position, now he is 5.
// Marc Marquez overtook Jorge Lorenzo!
// Marc Marquez is out of the race because of a technical issue, 10 laps before the finish.
// Valentino Rossi
//   Final position: 1
// Jorge Lorenzo
//   Final position: 3
// Johann Zarco
//   Final position: 5
