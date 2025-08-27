//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (startDate) => {
  // Convert startDate to milliseconds since Epoch
  let startMillis = startDate instanceof Date ? startDate.getTime() : Date.parse(startDate);
  
  // Calculate gigasecond in milliseconds (1,000,000,000 seconds)
  const gigasecondInMilliseconds = 1e9 * 1000; // 1e9 seconds * 1000 milliseconds
  
  // Addd gigasecond to startMillis
  let endMillis = startMillis + gigasecondInMilliseconds;
  
  // Create a new Date object from the endMillis timestamp
  return new Date(endMillis);
};