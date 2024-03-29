function merge_sort(arr) {
	// primeste un array si returneaza un array sortat
	var l = arr.length;
	if (l === 1)
		return arr;
	else {
		var x = arr.slice(0, Math.floor(l / 2)),
				y = arr.slice(Math.floor(l / 2), l),
				left = merge_sort(x),
				right = merge_sort(y),
				out = merge(left,right);
		return out;
	}
}

function merge(left, right) {
	// primeste doua arrayuri sortate si intoarce un array sortat rezultat din concatenarea arrayurilor de la intrare
	var  out=[],
		i = 0,
		j = 0,
		l1 = left.length,
		l2 = right.length;
	while (i<l1 && j<l2){
		if(left[i]<right[j]){
			out.push(left[i]);
			i++;
		} else {
			out.push(right[j]);
			j++;
		}			
	}
	if (i===l1){
		out=out.concat(right.slice(j,l2));
	}
	if (j===l2){
		out=out.concat(left.slice(i,l1));
	}
	return out;
}

var result = merge_sort([4,5,2,3,0,14,34]);
console.log(result);
