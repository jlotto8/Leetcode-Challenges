/*

*/

var numberOfEmployeesWhoMetTarget = function(hours, target) {
    let targetAchieved = 0;
    for(let i = 0; i < hours.length; i++){
        if(hours[i] >= target){
            targetAchieved++;
        }
    }
    return targetAchieved;
};

let result = numberOfEmployeesWhoMetTarget([5,1,4,2,2],6);
console.log(result);
