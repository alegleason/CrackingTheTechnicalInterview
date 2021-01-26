
function sum(a, b){
	while(b > 0){
		/*I am simply removing individual elements from a and adding them to b those same times*/
		a++;
		b--;
	}
	console.log(a);
	return a;
}

sum(1, 2);