<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {

name: 'hello',

data () {

return {

msg: 'Welcome to Your Vue.js App',

userName: '',

age: ''

}

},

methods: {

addUser() {

var name = this.userName;

var age = this.age;

this.$http.post('/api/user/addUser', {

username: name,

age: age

},{}).then((response) => {

console.log(response);

})

}

}

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
