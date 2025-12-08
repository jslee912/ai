function sumAll(){
  let result = 0;
  if(arguments.length==0){
    result = -999;
  }else if(arguments.length >=1){
    for(let data of arguments){
      result+=data;
    }
  }
  return result;
}