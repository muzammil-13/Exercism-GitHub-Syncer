// @ts-check

/**
 * Determine how many cards of a certain type there are in the deck
 *
 * @param {number[]} stack
 * @param {number} card
 *
 * @returns {number} number of cards of a single type there are in the deck
 */
export function cardTypeCheck(stack, card) {
  let count = 0;
  stack.forEach(c => {
    if (c === card) {
      count++;
    }
  });
  return count;
}

/**
 * Dettermine how many cards are odd or even
 *
 * @param {number[]} stack
 * @param {boolean} type the type of value to check for - odd or even
 * @returns {number} number of cards that are either odd or even (depending on `type`)
 */
export function determineOddEvenCards(stack, type) {
  let count = 0;
  for (const card of stack) {
    if (type && card % 2 === 0) { // even
      count++;
    } else if (!type && card % 2 !== 0) { // odd
      count++;
    }
  }
  return count;
}

// Example usage:
const cardType = 3;
console.log(cardTypeCheck([1, 2, 3, 4], cardType)); // => 1

console.log(determineOddEvenCards([1, 2, 3, 1, 5, 6], true)); // => 2
console.log(determineOddEvenCards([1, 2, 3, 1, 5, 6], false)); // => 4