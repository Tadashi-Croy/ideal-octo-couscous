
base_app = new Vue({
    el: '#base-head',
    delimiters: ['[[',']]'],
    data:{
        stuff: 'things',
    }
})


app = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        message: 'test'
    },


})