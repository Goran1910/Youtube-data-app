export class MergeSort<Type>{

    merge(collection: Type[], l: number, m: number, r: number, property: String, order: String){
        let p = property as keyof Type;
        
        var n1 = m - l + 1;
        var n2 = r - m;
    
        var L = new Array(n1);
        var R = new Array(n2);
    
        for (var i = 0; i < n1; i++)
            L[i] = collection[l + i];
        for (var j = 0; j < n2; j++)
            R[j] = collection[m + 1 + j];
    
        var i = 0;
        var j = 0;
        var k = l;
    
        while (i < n1 && j < n2) {
            if(order === 'asc'){
                if (L[i][p] <= R[j][p]) {
                    collection[k] = L[i];
                    i++;
                }
                else {
                    collection[k] = R[j];
                    j++;
                }
                k++;
            } else{
                if (L[i][p] > R[j][p]) {
                    collection[k] = L[i];
                    i++;
                }
                else {
                    collection[k] = R[j];
                    j++;
                }
                k++;
            }

        }
    
        while (i < n1) {
            collection[k] = L[i];
            i++;
            k++;
        }
    
        while (j < n2) {
            collection[k] = R[j];
            j++;
            k++;
        }
    }

    sort(collection: Type[], l: number, r: number, property: String, order: String){
        if(l >= r){
            return;
        }
        var m = l + Math.floor((r-l) / 2);
        this.sort(collection, l, m, property, order);
        this.sort(collection, m + 1, r, property, order);
        this.merge(collection, l, m, r, property, order);
    }

}