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
  }
  render() {
    return (
      <div>
        <h1> Welcome </h1>
        {/* Todo */}
        {/* {user email} */}
        <Typography color="textSecondary" variant='h2' gutterBottom>
          p4firebase@gmail.com
        </Typography>
        <h1> Latest Email </h1>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              sender - .........
            </Typography>
            <Typography variant="h5" component="h2">
              subject :- fasdafs
            </Typography>
            <Typography color="textSecondary">
              hashes found
            </Typography>
            <Typography color="textSecondary">
              urls found
            </Typography>
            <Typography color="textSecondary">
              hashes found
            </Typography>

            <Typography variant="body2" component="p">
              Attachments
              <br />
              Report of Attachment
            </Typography>
          </CardContent>
        </Card>

      </div>
    )
  }
}
