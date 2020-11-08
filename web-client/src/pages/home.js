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
    })
    .catch((error) => {
      console.error('Error:', error);
    });

    fetch('http://127.0.0.1:5000/report')
    .then(response => response.json())
    .then(data => {
      this.setState({report : {data}})
      if(data.positives > 0){
        this.setState({isMalware : true})
      }
      var positives = [] , negatives = []
      var cntp = 0 , cntn = 0;
      for(var ele in data.scans){
        if(data.scans[ele].detected == true){
          if(cntp >= 3){
            continue;
          }
          const element = {
            antivirus: ele,
            result : data.scans[ele].result
          }
          positives.push(element)
          cntp++;
        }else{
          if(cntn >= 3){
            continue;
          }
          const element = {
            antivirus: ele,
            result : data.scans[ele].result
          }
          negatives.push(element)
          cntn++;
        }
      }
      this.setState({positives : positives , negatives : negatives})
      
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
          {this.state.user}
        </Typography>
        <Typography variant="h2" color={"primary"}> Latest Email </Typography>
        <Card>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              sender - {this.state.sender}
            </Typography>
            <Typography variant="h5" component="h2" gutterBottom>
              subject :- {this.state.subject}
            </Typography>
            <Typography color="textSecondary" gutterBottom>
              <b>hashes found in body</b>
              <br/>
              sha1 :- {this.state.sha1}<br/>
              sha256 :- {this.state.sha256}<br/>
              md5 :- {this.state.md5}<br/>
            </Typography>
            <Typography color="textSecondary" gutterBottom>
              <b>URLs Found  in body</b><br/>
              {this.state.url}
            </Typography>

            <h3>Attachments</h3>
            <Typography color='primary'gutterBottom>
              <b>{this.state.attachment}</b>
            </Typography>
          </CardContent>
        </Card>

        <Card>
          <CardContent>

          <Typography variant="h5" component="h2" color={"secondary"}>
              Report of Attachment
            </Typography>
            <br/>
            {this.state.positives 
            ? <Typography color="textSecondary" variant="h3">
              Malware Found
            </Typography>
            : <Typography color="textSecondary" variant="h3">
            Malware Not Found
            </Typography>}
              <br/>
          {
            this.state.positives || this.state.negatives
            ?<Typography color="textSecondary" gutterBottom>
            <b>hashes found in attachment</b>
            <br/>
            sha1 :- {this.state.report.data.sha1}<br/>
            sha256 :- {this.state.report.data.sha256}<br/>
            md5 :- {this.state.report.data.md5}<br/>
          </Typography>
            :<h2> No attachments</h2>
          }
          {this.state.positives 
            ? this.state.positives.map((value, index) => {
              return (<div key={index}>
                <h3>{value.antivirus}</h3>
                Malware found - {value.result}
                </div> )
            })
            : (<h1>no positives</h1>)
          }
          
          {this.state.negatives 
            ? this.state.negatives.map((value, index) => {
              return (<div key={index}>
                <h3>{value.antivirus}</h3>
                Malware found - Not found
                </div> )
            })
            : (<h1>no negatives</h1>)
          }

          </CardContent>
        </Card>

        

      </div>
    )
  }
}
