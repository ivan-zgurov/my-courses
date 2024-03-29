function roadRadar(speed = 0, area = "") {
  const limits = { motorway: 130, interstate: 90, city: 50, residential: 20 };
  if (speed <= limits[area]) {
    console.log(`Driving ${speed} km/h in a ${limits[area]} zone`);
  } else {
    let difference = speed - limits[area];
    let violation = "";
    if (difference <= 20) {
      violation = "speeding";
    } else if (difference > 20 && difference <= 40) {
      violation = "excessive speeding";
    } else {
      violation = "reckless driving";
    }
    console.log(
      `The speed is ${difference} km/h faster than the allowed speed of ${limits[area]} - ${violation}`
    );
  }
}
