var createCounter = function(init) {
let current = init;
const original = init;
return{
     increment:function(){
        current++;
        return current;
  },
     decrement:function(){
        current --;
        return current;
    },

     reset:function(){
        current = original;
        return current;
    }
};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */