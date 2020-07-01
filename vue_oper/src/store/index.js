/**
 * @file main store
 * @author ielgnaw <wuji0223@gmail.com>
 */

import Vue from 'vue'
import Vuex from 'vuex'

import example from './modules/example'
import http from '@/api'
import { unifyObjectStyle } from '@/common/util'

Vue.use(Vuex)

const store = new Vuex.Store({
    // 模块
    modules: {
        example
    },
    // 公共 store
    state: {
        mainContentLoading: false,
        // 系统当前登录用户
        user: {}
    },
    // 公共 getters
    getters: {
        mainContentLoading: state => state.mainContentLoading,
        user: state => state.user
    },
    // 公共 mutations
    mutations: {},
    actions: {
        /**
         * 获取用户信息
         *
         * @param {Object} context store 上下文对象 { commit, state, dispatch }
         *
         * @return {Promise} promise 对象
         */
        userInfo (context, config = {}) {
            // ajax 地址为 USER_INFO_URL，如果需要 mock，那么只需要在 url 后加上 AJAX_MOCK_PARAM 的参数，
            // 参数值为 mock/ajax 下的路径和文件名，然后加上 invoke 参数，参数值为 AJAX_MOCK_PARAM 参数指向的文件里的方法名
            // 例如本例子里，ajax 地址为 USER_INFO_URL，mock 地址为 USER_INFO_URL?AJAX_MOCK_PARAM=index&invoke=getUserInfo

            // 后端提供的地址
            // const url = USER_INFO_URL
            // mock 的地址，示例先使用 mock 地址
            const mockUrl = USER_INFO_URL
            // + (USER_INFO_URL.indexOf('?') === -1 ? '?' : '&') + AJAX_MOCK_PARAM + '=index&invoke=getUserInfo'
            return http.get(mockUrl, {}, config).then(response => {
                const userData = response.data || {}
                context.commit('updateUser', userData)
                return userData
            })
        },
        search_business (context, config = {}) {
            return http.get('search_business/').then(response => {
                const data = response.data || {}
                return data
            })
        },
        fast_execute_script (context, param, config = {}) {
            return http.post('fast_execute_script/', param, config).then(response => {
                const data = response.data || {}
                return data
            })
        },
        search_host (context, param, config = {}) {
            return http.post('search_host/', param, config).then(response => {
                const data = response.data || {}
                return data
            })
        },
        delete_task (context, param, config = {}) {
            return http.post('task/delete_task/', param, config).then(response => {
                const data = response.data || {}
                return data
            })
        },
        get_task (context, config = {}) {
            return http.get('get_task/').then(response => {
                const data = response.data || {}
                return data
            })
        },
        get_task_by_id (context, param, config = {}) {
            return http.post('task/get_task_by_id/', param, config).then(response => {
                const data = response.data || {}
                return data
            })
        },
        save_task (context, param, config = {}) {
            return http.post('task/edit_task/', param, config).then(response => {
                const data = response.data || {}
                return data
            })
        },
        get_oper (context, config = {}) {
            return http.get('get_operation/').then(response => {
                const data = response.data || {}
                return data
            })
        },
        get_user (context, config = {}) {
            return http.get('get_user/').then(response => {
                const data = response.data || {}
                return data
            })
        }
    }
})

/**
 * hack vuex dispatch, add third parameter `config` to the dispatch method
 *
 * @param {Object|string} _type vuex type
 * @param {Object} _payload vuex payload
 * @param {Object} config config 参数，主要指 http 的参数，详见 src/api/index initConfig
 *
 * @return {Promise} 执行请求的 promise
 */
store.dispatch = function (_type, _payload, config = {}) {
    const { type, payload } = unifyObjectStyle(_type, _payload)

    const action = { type, payload, config }
    const entry = store._actions[type]
    if (!entry) {
        if (NODE_ENV !== 'production') {
            console.error(`[vuex] unknown action type: ${type}`)
        }
        return
    }

    store._actionSubscribers.forEach(sub => {
        return sub(action, store.state)
    })

    return entry.length > 1
        ? Promise.all(entry.map(handler => handler(payload, config)))
        : entry[0](payload, config)
}

export default store
