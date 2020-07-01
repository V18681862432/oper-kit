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
                            <li class="king-navbar-active"><a href="/t/oper-kit/#/history">执行记录</a></li>
                            <li><a href="/t/oper-kit/#/script">管理任务</a></li>
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
            <div class="panel-heading"><i class="fa fa-list-ulx"></i> 记录列表
            </div>
            <div class="panel-content">
                <table class="table table-header-bg table-hover mb0" id="table_demo2">
                    <thead>
                        <tr>
                            <th>序号</th>
                            <th>用户</th>
                            <th style="width: 25%">开始时间</th>
                            <th style="width: 25%">结束时间</th>
                            <th>业务</th>
                            <th>状态</th>
                            <th>脚本id</th>
                            <th>机器数</th>
                        </tr>
                    </thead>
                    <tbody id="host_body">
                        <tr v-for="(item,index) in operationList" v-bind="item" :key="index">
                            <th>{{index + 1}}</th>
                            <th>{{item.user}}</th>
                            <th>{{item.start_time}}</th>
                            <th>{{item.end_time}}</th>
                            <th>{{item.biz}}</th>
                            <th>{{item.result}}</th>
                            <th>{{item.script_id}}</th>
                            <th>{{item.machine_numbers}}</th>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'history',
        data () {
            return {
                user: '',
                operationList: []
            }
        },
        created () {
            this.get_user()
            this.get_oper()
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
            async get_oper () {
                try {
                    const data = await this.$store.dispatch('get_oper', {}, { fromCache: true })
                    this.operationList = data
                    console.log(this.user)
                } catch (e) {
                    console.error(e)
                }
            }
        }
    }
</script>

<style scoped>

</style>
