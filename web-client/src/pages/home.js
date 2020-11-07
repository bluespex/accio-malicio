import React, { Component } from 'react'
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

export default class home extends Component {
  constructor(props) {
    super(props)
    this.state = {
      
    }
  }
  componentDidMount() {
    fetch('http://127.0.0.1:5000/')
    .then(response => response.json())
    .then(data => {
      this.setState(data)
      console.log(this.state)
    })
    .catch((error) => {
      console.error('Error:', error);
    });

    fetch('http://127.0.0.1:5000/report')
    .then(response => response.json())
    .then(data => {
      this.setState({report : {data}})
      console.log(this.state)
    })
    .catch((error) => {
      console.error('Error:', error);
    });

    // var positives = []
    // for(ele in this.state.report.data.scans){
    //   if(this.state.report.data.scans[ele].detected == true){
    //     positives.push({antivirus : {ele}})
    //   }
    // }
  }
  render() {
    return (
      <div>
        <h1> Welcome </h1>
        {/* Todo */}
        {/* {user email} */}
        <Typography color="textSecondary" variant='h2' gutterBottom>
          {this.state.user}
        </Typography>
        <h1> Latest Email </h1>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              sender - {this.state.sender}
            </Typography>
            <Typography variant="h5" component="h2">
              subject :- {this.state.subject}
            </Typography>
            <Typography color="textSecondary">
              hashes found
              sha1 :- {this.state.sha1}
              sha256 :- {this.state.sha256}
              md5 :- {this.state.md5}
            </Typography>
            <Typography color="textSecondary">
              {this.state.url}
            </Typography>

            <Typography variant="body2" component="p">
              Attachments
              <br />
              {this.state.attachment}
            </Typography>
          </CardContent>
        </Card>

        

      </div>
    )
  }
}
