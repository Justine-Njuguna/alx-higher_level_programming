#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Count occurrences using reduce
  return list.reduce((count, element) => count + (element === searchElement), 0);
};
