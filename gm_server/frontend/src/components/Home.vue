<template>
<div class="home">
<el-row>
<el-table :data="userList" style="width: 100%" border>
<el-table-column prop="id" label="编号" min-width="100">
<template slot-scope="scope"> {{ scope.row.pk }} </template>
</el-table-column>
<el-table-column prop="username" label="用户名" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.username }} </template>
</el-table-column>
<el-table-column prop="department" label="部门" min-width="100">
<template slot-scope="scope"> {{ scope.row.fields.department }} </template>
</el-table-column>
</el-table>
    </el-row>
  </div>
</template>
<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      userList: []
    }
  },
  mounted: function () {
    this.show_user()
  },
  methods: {
    show_user () {
      this.$http.get('http://127.0.0.1:8000/login/show_user')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.userList = res['list']
          } else {
            this.$message.error('查询用户失败')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
