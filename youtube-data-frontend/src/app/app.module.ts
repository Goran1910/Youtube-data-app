import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ChannelsListComponent } from './components/channels-list/channels-list.component';
import { ChannelComponent } from './components/channel/channel.component';
import { HttpClientModule } from '@angular/common/http';
import { Router, RouterModule, Routes } from '@angular/router';
import { ChannelPageComponent } from './components/channel-page/channel-page.component';
import { ChannelInfoComponent } from './components/channel-info/channel-info.component';
import { VideoTableComponent } from './components/video-table/video-table.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { PlaylistTableComponent } from './components/playlist-table/playlist-table.component';
import { ComboAlbumsComponent } from './components/combo-albums/combo-albums.component';
import { FormsModule } from '@angular/forms';
import { HeaderComponent } from './components/header/header.component';

const appRoutes: Routes = [
  { path: '', component: ChannelsListComponent },
  { path: 'channels/:name', component: ChannelPageComponent, children: [
    { path: 'videos', component: VideoTableComponent },
    { path: 'playlists', component: PlaylistTableComponent }
  ]},

];

@NgModule({
  declarations: [
    AppComponent,
    ChannelsListComponent,
    ChannelComponent,
    ChannelPageComponent,
    ChannelInfoComponent,
    VideoTableComponent,
    PlaylistTableComponent,
    ComboAlbumsComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule, // MORA DA SE DODA
    RouterModule.forRoot(appRoutes), FontAwesomeModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
