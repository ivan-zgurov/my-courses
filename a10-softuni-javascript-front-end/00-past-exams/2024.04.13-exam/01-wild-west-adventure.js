function wildWestAdventure(input) {
  const n = Number(input.shift());
  const posse = {};

  for (let i = 0; i < n; i++) {
    const [name, hp, bullets] = input.shift().split(" ");
    posse[name] = {
      hp: Number(hp),
      bullets: Number(bullets),
    };
  }

  for (let commandLine of input) {
    if (commandLine === "Ride Off Into Sunset") {
      break;
    }

    const [command, ...args] = commandLine.split(" - ");
    const characterName = args[0];

    switch (command) {
      case "FireShot": {
        if (posse[characterName].bullets > 0) {
          posse[characterName].bullets--;
          console.log(
            `${characterName} has successfully hit ${args[1]} and now has ${posse[characterName].bullets} bullets!`
          );
        } else {
          console.log(
            `${characterName} doesn't have enough bullets to shoot at ${args[1]}!`
          );
        }
        break;
      }

      case "TakeHit": {
        const damage = Number(args[1]);
        const attacker = args[2];
        posse[characterName].hp -= damage;
        if (posse[characterName].hp > 0) {
          console.log(
            `${characterName} took a hit for ${damage} HP from ${attacker} and now has ${posse[characterName].hp} HP!`
          );
        } else {
          console.log(`${characterName} was gunned down by ${attacker}!`);
          delete posse[characterName];
        }
        break;
      }

      case "Reload": {
        const currentBullets = posse[characterName].bullets;
        if (currentBullets < 6) {
          const bulletsReloaded = 6 - currentBullets;
          posse[characterName].bullets = 6;
          console.log(`${characterName} reloaded ${bulletsReloaded} bullets!`);
        } else {
          console.log(`${characterName}'s pistol is fully loaded!`);
        }
        break;
      }

      case "PatchUp": {
        const healAmount = Number(args[1]);
        const currentHp = posse[characterName].hp;
        if (currentHp < 100) {
          const healedHp = Math.min(100 - currentHp, healAmount);
          posse[characterName].hp += healedHp;
          console.log(
            `${characterName} patched up and recovered ${healedHp} HP!`
          );
        } else {
          console.log(`${characterName} is in full health!`);
        }
        break;
      }

      default:
        break;
    }
  }

  for (const [name, stats] of Object.entries(posse)) {
    console.log(`${name}\n  HP: ${stats.hp}\n  Bullets: ${stats.bullets}`);
  }
}

// Test Case # 1 :

wildWestAdventure([
  "2",
  "Jesse 100 4",
  "Walt 100 5",
  "FireShot - Jesse - Bandit",
  "TakeHit - Walt - 30 - Bandit",
  "PatchUp - Walt - 20",
  "Reload - Jesse",
  "Ride Off Into Sunset",
]);

// Expected output:
// Jesse has successfully hit Bandit and now has 3 bullets!
// Walt took a hit for 30 HP from Bandit and now has 70 HP!
// Walt patched up and recovered 20 HP!
// Jesse reloaded 3 bullets!
// Jesse
//   HP: 100
//   Bullets: 6
// Walt
//   HP: 90
//   Bullets: 5

// Test Case # 2 :

wildWestAdventure([
  "2",
  "Gus 100 4",
  "Walt 100 5",
  "FireShot - Gus - Bandit",
  "TakeHit - Walt - 100 - Bandit",
  "Reload - Gus",
  "Ride Off Into Sunset",
]);

// Expected output:
// Gus has successfully hit Bandit and now has 3 bullets!
// Walt was gunned down by Bandit!
// Gus reloaded 3 bullets!
// Gus
//   HP: 100
//   Bullets: 6
