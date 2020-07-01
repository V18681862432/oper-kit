<template>
    <div>
        <div>
            <button class="king-btn mr5 king-success"><a href="/t/oper-kit/#/script" style="color: white">返回</a></button>
        </div>
        <center>
            <div>
                名称：<input type="text" v-model="taskName"> <br />
                内容：<textarea type="text" v-model="taskContent" rows="25" cols="100"> </textarea> <br />
                默认参数：<input type="text" v-model="taskParams"> <br />
                描述：<input type="text" v-model="taskDesc"> <br />
            </div>
            <div>
                <button @click="save_task()" class="king-btn mr5 king-success">保存</button>
            </div>
        </center>

    </div>

</template>

<script>
    export default {
        name: 'add',
        data () {
            return {
                'task': '',
                'taskId': '',
                'taskName': '',
                'taskContent': '',
                'taskParams': '',
                'taskDesc': ''
            }
        },
        mounted () {
            const params = this.$route.params
            if (isNaN(params.task_id) === false) {
                this.taskId = params.task_id
                this.get_task_by_id()
            }
        },
        methods: {
            async get_task_by_id () {
                try {
                    const data = await this.$store.dispatch('get_task_by_id', { task_id: this.taskId }, { cancelPrevious: false })
                    this.task = data
                    this.taskName = this.task.script_name
                    this.taskContent = this.task.script_content
                    this.taskParams = this.task.default_params
                    this.taskDesc = this.task.script_desc
                } catch (e) {
                    console.error(e)
                }
            },
            async save_task () {
                try {
                    const data = await this.$store.dispatch('save_task', {
                        task_id: this.taskId,
                        task_name: this.taskName,
                        task_content: this.taskContent,
                        task_params: this.taskParams,
                        task_desc: this.taskDesc
                    }, { cancelPrevious: false })
                    alert(data)
                } catch (e) {
                    console.error(e)
                }
            }
        }
    }
</script>

<style scoped>

</style>
