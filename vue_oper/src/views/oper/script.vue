<template>
    <div class="king-page-box">
        <div class="king-layout1-header">
            <nav role="navigation" class="navbar navbar-default king-horizontal-nav2    f14 ">
                <div class="container " style="width:100%;overflow:hidden;">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle collapsed navbar-toggle-sm" data-toggle="collapse"
                            data-target="#king-horizontal-nav2-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="javascript:void(0);">
                            <img src="https://magicbox.bk.tencent.com/static_api/v3/bk/images/logo3.png" alt=""
                                class="logo"> </a>
                    </div>
                    <div class="collapse navbar-collapse navbar-responsive-collapse" id="king-horizontal-nav2-collapse">
                        <ul class="nav navbar-nav">
                            <li><a href="/t/oper-kit/#/">首页</a></li>
                            <li><a href="/t/oper-kit/#/history">执行记录</a></li>
                            <li class="king-navbar-active"><a href="/t/oper-kit/#/script">管理任务</a></li>
                        </ul>
                        <ul class="nav navbar-nav navbar-right">
                            <li>
                                <a href="javascript:void(0);">
                                    <span onload="get_user()">{{user}}</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
        <div class="panel panel-default pannel-overflow panel-tables table7_demo">
            <div class="panel-heading"><i class="fa fa-list-ulx"></i> 任务列表
            </div>
            <div class="panel-heading"><i class="fa fa-list-ulx"></i>
                <button href="javascript:void(0);" class="king-btn mr5 king-success" @click="edit_task()">增加任务</button>
            </div>
            <div class="panel-content">
                <table class="table table-header-bg table-hover mb0" id="table_demo2">
                    <thead>
                        <tr>
                            <th class="col-sm-3">序号</th>
                            <th>任务名</th>
                            <th class="col-sm-2">管理</th>
                        </tr>
                    </thead>
                    <tbody id="host_body">
                        <tr v-for="(item,index) in taskList" v-bind="item" :key="index">
                            <th class="col-sm-3">{{index + 1}}</th>
                            <th>{{item.script_name}}</th>
                            <th class="col-sm-4">
                                <button href="javascript:void(0);" @click="delete_task(item.id)"
                                    class="king-btn mr3  king-notice-fail">删除
                                </button>
                                <button href="javascript:void(0);" class="king-btn mr5 king-success"
                                    @click="edit_task(item.id)">修改
                                </button>
                            </th>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'edit',
        data () {
            return {
                user: '',
                taskList: ''
            }
        },
        created () {
            this.get_user()
            this.get_task()
        },
        methods: {
            async get_user () {
                try {
                    const data = await this.$store.dispatch('get_user', {}, { fromCache: true })
                    this.user = data
                    console.log(this.user)
                } catch (e) {
                    console.error(e)
                }
            },
            async get_task () {
                try {
                    const data = await this.$store.dispatch('get_task', {}, { fromCache: true })
                    this.taskList = data
                    console.log(this.taskList)
                } catch (e) {
                    console.error(e)
                }
            },
            edit_task (id) {
                this.$router.push({
                    path: '/edit',
                    name: 'edit',
                    params: {
                        task_id: id
                    }
                })
            },
            async delete_task (id) {
                try {
                    const data = await this.$store.dispatch('delete_task', { task_id: id }, { cancelPrevious: false })
                    this.hostList = data
                    console.log(this.hostList)
                } catch (e) {
                    console.error(e)
                }
            }
        }
    }
</script>

<style scoped>

</style>
