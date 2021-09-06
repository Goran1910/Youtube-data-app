import { Component, OnInit } from '@angular/core';
import { Channel } from 'src/app/Channel';
import { ChannelService } from 'src/app/services/channel.service';

@Component({
  selector: 'app-channels-list',
  templateUrl: './channels-list.component.html',
  styleUrls: ['./channels-list.component.css']
})
export class ChannelsListComponent implements OnInit {

  channels: Channel[] = [];

  constructor(private channelService: ChannelService) { }

  ngOnInit(): void {
    this.channelService.getChannels().subscribe((channels) => this.channels = channels);
  }

}
