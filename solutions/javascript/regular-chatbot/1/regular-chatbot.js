// @ts-check

/**
 * Given a certain command, help the chatbot recognize whether the command is valid or not.
 *
 * @param {string} command
 * @returns {boolean} whether or not is the command valid
 */
export function isValidCommand(command) {
  const regex = /^chatbot\b/i;
  return regex.test(command);
}

/**
 * Given a certain message, help the chatbot get rid of all the emoji's encryption through the message.
 *
 * @param {string} message
 * @returns {string} The message without the emojis encryption
 */
export function removeEmoji(message) {
  const regex = /emoji\d+/g;
  return message.replace(regex, '');
}

/**
 * Given a certain phone number, help the chatbot recognize whether it is in the correct format.
 *
 * @param {string} number
 * @returns {string} the Chatbot response to the phone Validation
 */
export function checkPhoneNumber(number) {
  const regex = /^\(\+\d{2}\) \d{3}-\d{3}-\d{3}$/;
  if (regex.test(number)) {
    return "Thanks! You can now download me to your phone.";
  } else {
    return `Oops, it seems like I can't reach out to ${number}`;
  }
}

/**
 * Given a certain response from the user, help the chatbot get only the URL.
 *
 * @param {string} userInput
 * @returns {string[] | null} all the possible URL's that the user may have answered
 */
export function getURL(userInput) {
  const regex = /\bhttps?:\/\/[^\s/$.?#].[^\s]*\b|(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b/gi;
  return userInput.match(regex);
}

/**
 * Greeet the user using the full name data from the profile.
 *
 * @param {string} fullName
 * @returns {string} Greeting from the chatbot
 */
export function niceToMeetYou(fullName) {
  const regex = /(\w+), (\w+)/;
  return fullName.replace(regex, 'Nice to meet you, $2 $1');
}

// Example usage:
console.log(isValidCommand("Chatbot, play a song from the 80's.")); // => True
console.log(isValidCommand("Hey Chatbot, where is the closest pharmacy?")); // => False
console.log(isValidCommand("CHATBOT, do you have a solution for this challenge?")); // => True

console.log(removeEmoji("I love playing videogames emoji3465 it's one of my hobbies"));
// => "I love playing videogames  it's one of my hobbies"

console.log(checkPhoneNumber('(+34) 659-771-594'));
// => "Thanks! You can now download me to your phone."
console.log(checkPhoneNumber('659-771-594'));
// => "Oops, it seems like I can't reach out to 659-771-594"

console.log(getURL('I learned a lot from https://exercism.org'));
// => ["https://exercism.org"]
console.log(getURL('Visit google.com and yahoo.com for more info'));
// => ["google.com", "yahoo.com"]

let str = 'Smith, John';
console.log(niceToMeetYou(str));
// => "Nice to meet you, John Smith"