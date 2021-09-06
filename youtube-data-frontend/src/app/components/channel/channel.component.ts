import { Component, Input, OnInit } from '@angular/core';
import { Channel } from 'src/app/Channel';
import { Router, ActivatedRoute } from '@angular/router';
import { ChannelService } from 'src/app/services/channel.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-channel',
  templateUrl: './channel.component.html',
  styleUrls: ['./channel.component.css']
})
export class ChannelComponent implements OnInit {

  @Input()
  channel!: Channel;

  channelFromService!: Channel;
  quearyParams = environment.defaultQueryParams;

  constructor(private route: ActivatedRoute, private router: Router, private channelService: ChannelService) { }

  ngOnInit(): void {
    /*this.route.queryParams
    .filter(params => params.name)
    .subscribe(params => {
        console.log(params);
        this.channelService.getChannel(params['name']).subscribe((channel) => {this.channel = channel});
    })*/
    let param = this.route.snapshot.queryParams['name'];
    if(param != undefined){
      this.channelService.getChannel(param).subscribe((channel) => {this.channelFromService = channel});
    }
  }

  hasRoute(route: String): Boolean{
    let urlPath = "";
    this.route.url.subscribe((url) => {
      urlPath = '/' + url.join('/'); 
    });
    return urlPath === route;
  }

}
