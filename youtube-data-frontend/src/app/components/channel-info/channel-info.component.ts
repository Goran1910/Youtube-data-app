import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Channel } from 'src/app/Channel';
import { ChannelService } from 'src/app/services/channel.service';

@Component({
  selector: 'app-channel-info',
  templateUrl: './channel-info.component.html',
  styleUrls: ['./channel-info.component.css']
})
export class ChannelInfoComponent implements OnInit {

  channel!: Channel;

  constructor(private route: ActivatedRoute, private channelService: ChannelService) { }

  ngOnInit(): void {
    
    this.route.paramMap.subscribe((params) => {
      let param = params.get('name');
      
      if (param != null) {
        this.channelService.getChannel(param).subscribe((channel) => this.channel = channel);
      }
    });
  }

}
