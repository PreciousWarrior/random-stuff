class Set {
    constructor(initialItems = [], maxSize = Number.POSITIVE_INFINITY) {
        this.set = []
        this.maxSize = maxSize
        this.add(...initialItems)
    }

    add(...items) {
        for (let item of items) {
            if (this.set.indexOf(item) === -1 && this.size < this.maxSize) {
                this.set.push(item)
            }
        }

        return this
    }

    get size() {
        return this.set.length
    }

    delete(...items) {
        for (let item of items) {
            let itemIndex = this.set.indexOf(item)
            if (itemIndex > -1) {
                this.set.splice(itemIndex, 1)
            }
        }

        return this
    }

    has(...items) {
        for (let item of items) {
            if (this.set.indexOf(item) === -1) {
                return false
            }
        }

        return true
    }

}

let mySet = new Set()
let key = {}
mySet.add(key)
console.log(mySet.size)
key = null
console.log(mySet.size)