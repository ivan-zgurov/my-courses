function cryptocurrencyDecoder(input) {
  let message = input.shift();

  // Process commands
  for (let commandLine of input) {
    if (commandLine === "Buy") {
      break;
    }

    const [command, ...args] = commandLine.split("?");

    switch (command) {
      case "TakeEven": {
        message = message
          .split("")
          .filter((_, index) => index % 2 === 0)
          .join("");
        console.log(message);
        break;
      }

      case "ChangeAll": {
        const [substring, replacement] = args;
        message = message.split(substring).join(replacement);
        console.log(message);
        break;
      }

      case "Reverse": {
        const substring = args[0];
        const index = message.indexOf(substring);

        if (index !== -1) {
          message =
            message.substring(0, index) +
            message.substring(index + substring.length);
          const reversedSubstring = substring.split("").reverse().join("");
          message += reversedSubstring;
          console.log(message);
        } else {
          console.log("error");
        }
        break;
      }

      default:
        break;
    }
  }

  console.log(`The cryptocurrency is: ${message}`);
}

// Test Case # 1:
cryptocurrencyDecoder([
  "z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
  "TakeEven",
  "Reverse?!nzahc",
  "ChangeAll?m?g",
  "Reverse?adshk",
  "ChangeAll?z?i",
  "Buy",
]);

// Expected output:
// ztsnotBztcoznztsVe!nzahc
// ztsnotBztcoznztsVechazn!
// ztsnotBztcoznztsVechazn!
// error
// itsnotBitcoinitsVechain!
// The cryptocurrency is: itsnotBitcoinitsVechain!

// Test Case # 2:
cryptocurrencyDecoder([
  "PZDfA2PkAsakhnefZ7aZ",
  "TakeEven",
  "TakeEven",
  "TakeEven",
  "ChangeAll?Z?X",
  "ChangeAll?A?R",
  "Reverse?PRX",
  "Buy",
]);

// Expected output:
// PDAPAaheZa
// PAAhZ
// PAZ
// PAX
// PRX
// XRP
// The cryptocurrency is: XRP
