
base_app = new Vue({
    el: '#base-head',
    delimiters: ['[[',']]'],
    data:{
        stuff: 'things',
    }
})


main_app = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        message: 'test',
        update: false,
        dog_update: false,
        addNewDogBTN: false,
        phone_number: '',
        first_name: '',
        last_name: '',
        address: '',
        city: '',
        zipcode: '',
        share_pupps:'',
        dog_name:'',
        age:'',
        sex:'',
        size:'',
        temperment:'',
        crate_trained:'',
        details:''


    },
    created() {
  
    },
    methods: {
        personalProfiler: async function(url_path){
            console.log('AddNewDog Function')
            
            let token = document.getElementsByName('csrfmiddlewaretoken')[0]
            
            let config = {
                method: 'POST',
                url : url_path,
                data: {
                    phone_number: this.phone_number,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    address: this.address,
                    city: this.city,
                    zipcode: this.zipcode,
                    share_pupps: this.share_pupps,
                    dog_name: this.dog_name,
                    age: this.age,
                    sex: this.sex,
                    size: this.size,
                    temperment: this.temperment,
                    crate_trained: this.crate_trained,
                    details: this.details,
                },
                headers:{
                    'X-CSRFToken': token.value
                }


            } 
            
            let response = await axios(config) 

            console.log(response)

            this.phone_number= '',
            this.first_name= '',
            this.last_name= '',
            this.address= '',
            this.city= '',
            this.zipcode= '',
            this.share_pupps='',
            this.dog_name='',
            this.age='',
            this.sex='',
            this.size='',
            this.temperment='',
            this.crate_trained='',
            this.details=''


        },
        updateDog: function(){
            console.log('UpdateDog Function')



        }
    },

})


