// @ts-check

/**
 * Removes duplicate tracks from a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} new playlist with unique entriess
 */
export function removeDuplicates(playlist) {
  return [...new Set(playlist)];
}

/**
 * Checks whether a playlist includes a track.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {boolean} whether the track is in the playlist
 */
export function hasTrack(playlist, track) {
  return playlist.includes(track);
}

/**
 * Adds a track to a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function addTrack(playlist, track) {
  if (!hasTrack(playlist, track)) {
    return [...playlist, track];
  }
  return playlist;
}

/**
 * Deletes a track from a playlist.
 *
 * @param {string[]} playlist
 * @param {string} track
 * @returns {string[]} new playlist
 */
export function deleteTrack(playlist, track) {
  return playlist.filter(t => t !== track);
}

/**
 * Lists the unique artists in a playlist.
 *
 * @param {string[]} playlist
 * @returns {string[]} list of artists
 */
export function listArtists(playlist) {
  const artists = playlist.map(track => track.split(' - ')[1]);
  return [...new Set(artists)];
}

// Example usage:
const playlist1 = [
  'Court and Spark - Joni Mitchell',
  'Big Yellow Taxi - Joni Mitchell',
  'Court and Spark - Joni Mitchell',
];
console.log(removeDuplicates(playlist1));
// => ['Court and Spark - Joni Mitchell', 'Big Yellow Taxi - Joni Mitchell']

const playlist2 = [
  'The Fashion Show - Grace Jones',
  'Dr. Funkenstein - Parliament',
];
console.log(hasTrack(playlist2, 'Dr. Funkenstein - Parliament'));
// => true
console.log(hasTrack(playlist2, 'Walking in the Rain - Grace Jones'));
// => false

const playlist3 = ['Selma - Bijelo Dugme'];
console.log(addTrack(playlist3, 'Atomic Dog - George Clinton'));
// => ['Selma - Bijelo Dugme', 'Atomic Dog - George Clinton']
console.log(addTrack(playlist3, 'Selma - Bijelo Dugme'));
// => ['Selma - Bijelo Dugme', 'Atomic Dog - George Clinton']

const playlist4 = [
  'The Treasure - Fra Lippo Lippi',
  'After the Fall - Klaus Nomi',
];
console.log(deleteTrack(playlist4, 'The Treasure - Fra Lippo Lippi'));
// => ['After the Fall - Klaus Nomi']
console.log(deleteTrack(playlist4, 'I Feel the Magic - Belinda Carlisle'));
// => ['The Treasure - Fra Lippo Lippi', 'After the Fall - Klaus Nomi']

const playlist5 = [
  'All Mine - Portishead',
  'Sight to Behold - Devendra Banhart',
  'Sour Times - Portishead',
];
console.log(listArtists(playlist5));
// => ['Portishead', 'Devendra Banhart']