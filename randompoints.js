function getRandomPointDistance(sideLen) {
    var point1 = [Math.random() * sideLen, Math.random() * sideLen]
    var point2 = [Math.random() * sideLen, Math.random() * sideLen]
    var distance = Math.sqrt(Math.pow((point1[0] - point2[0]), 2) + Math.pow((point1[1] - point2[1]), 2))
    return distance
}

function getAveragePointDistanceInSquare(sideLen = 1, trials = 10000) {
    var total = 0
    for (var trial = 0; trial < trials; trial++) {
        total += getRandomPointDistance(sideLen)
    }
    return total / trials
}

console.log(getAveragePointDistanceInSquare())