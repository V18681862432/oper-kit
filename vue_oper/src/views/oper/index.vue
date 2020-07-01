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
                            <li class="king-navbar-active"><a href="/t/oper-kit/#/">首页</a></li>
                            <li><a href="/t/oper-kit/#/history">执行记录</a></li>
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
        <div class="king-layout2-main mt15" style="width:960px;">
            <form class="form-horizontal">
                <div class="form-group clearfix ">
                    <label class="col-sm-3 control-label bk-lh30 pt0">选择业务：</label>
                    <div class="col-sm-9">
                        <select name="" id="business" class="form-control bk-valign-top" @change="get_biz_list($event)">
                            <option value="">请选择</option>
                            <option v-for="item in bizList" v-bind:value="item.id" :key="item.id">{{item.name}}</option>
                        </select>
                    </div>
                </div>
                <div class="form-group clearfix ">
                    <label class="col-sm-3 control-label bk-lh30 pt0">任务类型：</label>
                    <div class="col-sm-9">
                        <select name="" id="task" class="form-control bk-valign-top" @change="get_task($event)">
                            <option value="">请选择</option>
                            <option v-for="item in taskList" v-bind:value="item.id" :key="item.id">{{item.script_name}}
                            </option>
                        </select>
                    </div>
                </div>
                <div class="form-group clearfix ">
                    <label class="col-sm-3 control-label bk-lh30 pt0">脚本参数：</label>
                    <div class="col-sm-9">
                        <input type="text" class="form-control bk-valign-top" v-model="scriptParam"
                            placeholder="请输入脚本参数,以分号隔开">
                    </div>
                </div>
                <div class="form-group clearfix">
                    <div class="col-sm-9 col-sm-offset-3">
                        <button href="javascript:void(0)" type="button"
                            class="king-btn mr10  king-success" @click="fast_execute_script()">执行
                        </button>
                    </div>
                </div>
            </form>
            <div class="panel panel-default pannel-overflow panel-tables table7_demo">
                <div class="panel-heading"><i class="fa fa-list-ulx"></i> 主机列表
                </div>
                <div class="panel-content">
                    <table class="table table-header-bg table-hover mb0" id="table_demo2">
                        <thead>
                            <tr>
                                <th style="width: 25px">
                                    <input type="checkbox" id="checkbox" v-model="checked" @change="changeAllChecked">
                                </th>
                                <th style="width: 100px">序号</th>
                                <th style="width:25%">内网IP</th>
                                <th style="width:25%">操作系统</th>
                            </tr>
                        </thead>
                        <tbody id="host_body">
                            <tr v-for="(item,index) in hostList" v-bind="item" :key="index">
                                <th style="width: 25px">
                                    <input type="checkbox" name="checkall" :id="item" v-model="checkedNames" :value="item">
                                </th>
                                <th>{{index + 1}}</th>
                                <th>{{item.ip}}</th>
                                <th>{{item.os_name}}</th>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import 'axios'

    export default {
        data () {
            return {
                checked: false,
                user: '',
                bkBizId: '',
                checkedNames: [],
                bizList: [],
                hostList: [],
                taskList: [],
                scriptParam: '',
                taskId: ''
            }
        },
        watch: {
            'checkedNames': function () {
                if (this.host_list.length === this.checkedNames.length) {
                    this.checked = true
                } else {
                    this.checked = false
                }
            }
        },
        created () {
            this.get_user()
            this.get_biz_list()
            this.get_task()
        },
        methods: {
            async get_biz_list (e) {
                try {
                    const data = await this.$store.dispatch('search_business', {}, { fromCache: true })
                    this.bizList = data
                    this.bkBizId = e.target.value
                    this.search_host()
                    console.log(this.bizList)
                } catch (e) {
                    console.error(e)
                }
            },
            async get_user () {
                try {
                    const data = await this.$store.dispatch('get_user', {}, { fromCache: true })
                    this.user = data
                    console.log(this.user)
                } catch (e) {
                    console.error(e)
                }
            },
            async get_task (e) {
                try {
                    const data = await this.$store.dispatch('get_task', {}, { fromCache: true })
                    this.taskList = data
                    this.taskId = e.target.value
                    console.log(this.taskList)
                } catch (e) {
                    console.error(e)
                }
            },
            async search_host () {
                try {
                    const data = await this.$store.dispatch('search_host', { bk_biz_id: this.bkBizId }, { cancelPrevious: false })
                    this.hostList = data
                    console.log(this.hostList)
                } catch (e) {
                    console.error(e)
                }
            },
            async fast_execute_script () {
                const ipList = new Array(this.checkedNames.length)
                for (let i = 0; i < this.checkedNames.length; i++) {
                    ipList[i] = { 'ip': this.checkedNames[i]['ip'] }
                }
                try {
                    const data = await this.$store.dispatch('fast_execute_script', {
                        bk_biz_id: this.bkBizId,
                        ip_list: ipList,
                        task_id: this.taskId,
                        script_param: this.scriptParam,
                        user: this.user
                    }, { cancelPrevious: false })
                    alert(data)
                    console.log(this.hostList)
                } catch (e) {
                    console.error(e)
                }
            },
            changeAllChecked () {
                if (this.checked) {
                    this.checkedNames = this.hostList
                } else {
                    this.checkedNames = []
                }
            }
        }
    }
</script>

<style scoped>

</style>
