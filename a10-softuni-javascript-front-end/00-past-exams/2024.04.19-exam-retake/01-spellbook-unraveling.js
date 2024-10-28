function spellbookUnraveling(input) {
  let spell = input.shift();

  for (let commandLine of input) {
    if (commandLine === "End") {
      break;
    }

    const [command, ...args] = commandLine.split("!");

    switch (command) {
      case "RemoveEven":
        spell = spell
          .split("")
          .filter((_, index) => index % 2 === 0)
          .join("");
        console.log(spell);
        break;

      case "TakePart": {
        const fromIndex = Number(args[0]);
        const toIndex = Number(args[1]);
        spell = spell.substring(fromIndex, toIndex);
        console.log(spell);
        break;
      }

      case "Reverse": {
        const substring = args[0];
        const index = spell.indexOf(substring);

        if (index !== -1) {
          spell =
            spell.substring(0, index) +
            spell.substring(index + substring.length);
          const reversedSubstring = substring.split("").reverse().join("");
          spell += reversedSubstring;
          console.log(spell);
        } else {
          console.log("Error");
        }
        break;
      }

      default:
        break;
    }
  }

  console.log(`The concealed spell is: ${spell}`);
}

// Test Case # 1:
spellbookUnraveling([
  "asAsl2adkda2mdaczsa",
  "RemoveEven",
  "TakePart!1!9",
  "Reverse!maz",
  "End",
]);

// Expected output:
// aAlakamaza
// Alakamaz
// Alakazam
// The concealed spell is: Alakazam

// Test Case # 2:
spellbookUnraveling([
  "hZwemtroiui5tfone1haGnanbvcaploL2u2a2n2i2m",
  "TakePart!31!42",
  "RemoveEven",
  "Reverse!anim",
  "Reverse!sad",
  "End",
]);

// Expected output:
// L2u2a2n2i2m
// Luanim
// Lumina
// Error
// The concealed spell is: Lumina
