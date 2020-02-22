'use strict'
module.exports = {
  NODE_ENV: '"production"',
  VUE_APP_API_URL: JSON.stringify(`http://${process.env.BASE_URL}/api`)
}
