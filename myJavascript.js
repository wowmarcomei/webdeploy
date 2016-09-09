/*
//Setup
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["Javascript", "Gaming", "Foxes"]
    }
];


function lookUp(firstName, prop){
// Only change code below this line
    var result = 0;
    for(var i=0;i<contacts.length;i++){
        for(var j=0; j<Object.keys(contacts[i]).length; j++){
            if (contacts[i]['firstName'] == firstName){
                if (contacts[i].hasOwnProperty(prop)){
                    console.log(contacts[i][prop]);
                    return contacts[i][prop];
                } else {
                    return "No such property";
                }
            } else {
                result = "No such contact";
            }
        }
    }

    return result;
}

// Only change code above this line

// Change these values to test your function
lookUp("Akira", "address");

*/

/*
ex2: 查找最长的字符串
*/
function findLongestWord(str) {
    var myLength = [0];
    var newRes = 0;
    var myArray = str.split(" ");
    for (var i = 0; i<myArray.length; i++){
        myLength[i] = myArray[i].length;
    }

    myLength.sort(function (a,b) {
        return b-a;
    });
    return myLength[0];

}

console.log(findLongestWord("What if we try a super-long word such as otorhinolaryngology"));
findLongestWord("What if we try a super-long word such as otorhinolaryngology");

