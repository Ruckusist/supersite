import * as _ from 'lodash'
import * as React from 'react'
import * as ReactDOM from 'react-dom'
import { HelloWorld } from './helloworld'

import '../sass/main.scss'
import '../sass/animated_nav.scss'

ReactDOM.render(
  <HelloWorld/>,
  document.getElementById('root')
)

console.log('this is working')