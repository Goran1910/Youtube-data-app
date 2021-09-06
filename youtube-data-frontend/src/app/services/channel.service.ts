import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Channel } from '../Channel';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ChannelService {

  private apiUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getChannels(): Observable<Channel[]>{
    return this.http.get<Channel[]>('http://localhost:8080/channels');
  }

  getChannel(name: string): Observable<Channel>{
    return this.http.get<Channel>(`http://localhost:8080/channels/${name}`);
  }
}
