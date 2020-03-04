'use strict'
module.exports = {
  NODE_ENV: '"production"',
  VUE_APP_API_URL: JSON.stringify(`https://${process.env.BASE_URL}/api`)
}
