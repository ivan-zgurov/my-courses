function astroAdventure(input) {
  const n = Number(input.shift());
  const astronauts = {};

  for (let i = 0; i < n; i++) {
    const [name, oxygen, energy] = input.shift().split(" ");
    astronauts[name] = {
      oxygen: Number(oxygen),
      energy: Number(energy),
    };
  }

  for (let commandLine of input) {
    if (commandLine === "End") {
      break;
    }

    const [command, ...args] = commandLine.split(" - ");
    const astronautName = args[0];

    switch (command) {
      case "Explore": {
        const energyNeeded = Number(args[1]);
        if (astronauts[astronautName].energy >= energyNeeded) {
          astronauts[astronautName].energy -= energyNeeded;
          console.log(
            `${astronautName} has successfully explored a new area and now has ${astronauts[astronautName].energy} energy!`
          );
        } else {
          console.log(
            `${astronautName} does not have enough energy to explore!`
          );
        }
        break;
      }

      case "Refuel": {
        const amount = Number(args[1]);
        const currentEnergy = astronauts[astronautName].energy;
        const newEnergy = Math.min(currentEnergy + amount, 200);
        const recoveredEnergy = newEnergy - currentEnergy;
        astronauts[astronautName].energy = newEnergy;
        console.log(
          `${astronautName} refueled their energy by ${recoveredEnergy}!`
        );
        break;
      }

      case "Breathe": {
        const amount = Number(args[1]);
        const currentOxygen = astronauts[astronautName].oxygen;
        const newOxygen = Math.min(currentOxygen + amount, 100);
        const recoveredOxygen = newOxygen - currentOxygen;
        astronauts[astronautName].oxygen = newOxygen;
        console.log(
          `${astronautName} took a breath and recovered ${recoveredOxygen} oxygen!`
        );
        break;
      }

      default:
        break;
    }
  }

  for (const [name, details] of Object.entries(astronauts)) {
    console.log(
      `Astronaut: ${name}, Oxygen: ${details.oxygen}, Energy: ${details.energy}`
    );
  }
}

// Test Case #1:
astroAdventure([
  "3",
  "John 50 120",
  "Kate 80 180",
  "Rob 70 150",
  "Explore - John - 50",
  "Refuel - Kate - 30",
  "Breathe - Rob - 20",
  "End",
]);

// Expected output:
// John has successfully explored a new area and now has 70 energy!
// Kate refueled their energy by 20!
// Rob took a breath and recovered 20 oxygen!
// Astronaut: John, Oxygen: 50, Energy: 70
// Astronaut: Kate, Oxygen: 80, Energy: 200
// Astronaut: Rob, Oxygen: 90, Energy: 150

// Test Case #2:
astroAdventure([
  "4",
  "Alice 60 100",
  "Bob 40 80",
  "Charlie 70 150",
  "Dave 80 180",
  "Explore - Bob - 60",
  "Refuel - Alice - 30",
  "Breathe - Charlie - 50",
  "Refuel - Dave - 40",
  "Explore - Bob - 40",
  "Breathe - Charlie - 30",
  "Explore - Alice - 40",
  "End",
]);

// Expected output:
// Bob has successfully explored a new area and now has 20 energy!
// Alice refueled their energy by 30!
// Charlie took a breath and recovered 30 oxygen!
// Dave refueled their energy by 20!
// Bob does not have enough energy to explore!
// Charlie took a breath and recovered 0 oxygen!
// Alice has successfully explored a new area and now has 90 energy!
// Astronaut: Alice, Oxygen: 60, Energy: 90
// Astronaut: Bob, Oxygen: 40, Energy: 20
// Astronaut: Charlie, Oxygen: 100, Energy: 150
// Astronaut: Dave, Oxygen: 80, Energy: 200
